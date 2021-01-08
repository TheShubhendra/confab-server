from requests import post
from .helper import delete_tested_user


def test_check_username():
    url = 'http://127.0.0.1:5000/api/checkusername'
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
    req1 = post(url, json=data1)
    req2 = post(url, json=data2)
    assert req1.text == "1" and req2.text == "0"


def test_register():
    url = 'http://127.0.0.1:5000/api/register'
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
    req1 = post(url, json=data1)
    req2 = post(url, json=data2)
    delete_tested_user("newuser-register-test")
    assert req1.text == "1" and req2.text == "0"


if __name__ == '__main__':
    test_check_username()
    test_register()
