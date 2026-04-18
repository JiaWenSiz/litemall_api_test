def test_sample():
    assert 1 + 1 == 2

def test_api_status():
    import requests
    # 这里可以替换成你要测试的真实接口
    response = requests.get(https://httpbin.org/status/200)
    assert response.status_code == 200
