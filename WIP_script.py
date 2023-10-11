import requests
import pytest
def test_login_success():
    response = requests.post('placeholder site login', data=dict(username='admin', password='secret'))
    assert response.status_code == 200
    assert response.url == 'placeholde site home/dashboard'
def test_login_failure():
    response = requests.post('placeholder site login', data=dict(username='invalid_user', password='invalid_password'))
    assert response.status_code == 200
    assert response.url == 'placeholder site login'
def test_empty_login():
    response = requests.post('placeholder site login', data=dict(username='', password=''))
    assert response.status_code == 200
    assert response.url == 'placeholder site login'
if __name__ == "__main__":
    pytest.main()
