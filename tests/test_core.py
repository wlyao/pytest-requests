def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)

import requests

def test_httpbin_get():
    resp = requests.get(
        "http://www.httpbin.org/get",
        headers={"accept": "application/json"}
    )
    assert resp.status_code == 200
    assert resp.headers["server"] == "nginx"
    assert resp.json()["url"] == "https://www.httpbin.org/get"

def test_httpbin_get_with_prams():
    resp = requests.get(
        "http://www.httpbin.org/get",
        params={"abc": 123},
        headers={"accept": "application/json"}
    )
    assert resp.status_code == 200
    assert resp.headers["server"] == "nginx"
    assert resp.json()["url"] == "https://www.httpbin.org/get?abc=123"

def test_httpbin_post():
    resp = requests.post(
        "http://www.httpbin.org/post",
        data="abc=123",
        headers={"accept": "application/json"}
    )
    assert resp.status_code == 200
    assert resp.headers["server"] == "nginx"
    assert resp.json()["url"] == "https://www.httpbin.org/post"
    print("resp.json()==", resp.json())
    assert resp.json()["data"]== "abc=123"

def test_httpbin_post_json():
    resp = requests.post(
        "http://www.httpbin.org/post",
        json={"abc": 123},
        headers={"accept": "application/json"}
    )
    assert resp.status_code == 200
    assert resp.headers["server"] == "nginx"
    assert resp.json()["url"] == "https://www.httpbin.org/post"
    print("resp.json()==", resp.json())
    assert resp.json()["json"]["abc"] == 123