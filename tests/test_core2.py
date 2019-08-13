def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)

import requests
from hogwarts_apitest.api import BaseApi

class ApiHttpbinGet(BaseApi):
    url =  "http://www.httpbin.org/get"
    params = {}
    method = "GET"
    headers={"accept": "application/json"}


class ApiHttpbinPost(BaseApi):
    url =  "http://www.httpbin.org/post"
    method = "POST"
    headers={"accept": "application/json"}
    params = {}
    data = "abc=123"
    json={"abc": 123}


def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code", 200)\
        .validate("headers.server", "nginx")\
        # .validate("json.url", "https://www.httpbin.org/get")

    
def test_httpbin_get_with_params():
    ApiHttpbinGet()\
        .set_params(abc=123, xyz=456)\
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "nginx") \


def test_httpbin_post():
   ApiHttpbinPost()\
        .set_json({"abc": 123})\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.server", "nginx")\
        .validate("json().url", "https://www.httpbin.org/post")\
        .validate("json().args", {})\
        .validate("json().headers.Accept", "application/json")\
        .validate("json().json.abc", 123)


#
# def test_httpbin_post_json():
#     resp = requests.post(
#         "http://www.httpbin.org/post",
#         json={"abc": 123},
#         headers={"accept": "application/json"}
#     )
#     assert resp.status_code == 200
#     assert resp.headers["server"] == "nginx"
#     assert resp.json()["url"] == "https://www.httpbin.org/post"
#     # print("resp.json()==", resp.json())
#     assert resp.json()["json"]["abc"] == 123