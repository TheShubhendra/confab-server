from .helper import delete_tested_user


def test_check_username(client):
    url = '/api/checkusername'
    data1 = {
             "username": "available-username-availibilty-test",
             "password": "unit-test",
             "client_data": "unit-test",
    }
    data2 = {
             "username": "unavailable-username-availibilty-test",
             "password": "unit-test",
             "client_data": "unit-test",
    }
    res1 = client.post(url, json=data1)
    res2 = client.post(url, json=data2)
    assert res1.data == b"1" and res2.data == b"0"


def test_register(client):
    url = '/api/register'
    data1 = {
        "username": "newuser-register-test",
        "password": "unit-test",
        "client_data": "unit-test",
    }
    data2 = {
        "username": "olduser-register-test",
        "password": "unit-test",
        "client_data": "unit-test"
    }
    res1 = client.post(url, json=data1)
    res2 = client.post(url, json=data2)
    delete_tested_user("newuser-register-test")
    assert res1.data == b"1" and res2.data == b"0"
