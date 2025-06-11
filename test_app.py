import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    """测试根路由"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_status_route(client):
    """测试状态路由"""
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_echo_route(client):
    """测试回显路由"""
    test_data = {'message': 'test'}
    response = client.post('/api/echo', json=test_data)
    assert response.status_code == 200
    assert response.json == test_data 
