from fastapi.testclient import TestClient

from main import app
client = TestClient(app)

def test_1_get_count():
    '''
    When heads and legs are not sent
    '''
    response= client.get("/get_count")
    assert response.status_code==422

def test_2_get_count():
    '''
    When heads and legs are available and yields a success
    '''
    head_count=10
    leg_count=20
    response=client.get("/get_count", params={'head_count':head_count, 'leg_count':leg_count})
    assert response.status_code==200

def test_3_get_count():
    '''
    When heads are more than legs
    '''
    head_count=20
    leg_count=19
    response= client.get("/get_count", params={'head_count':head_count, 'leg_count':leg_count})
    assert response.status_code==400

def test_4_get_count():
    '''
    When head value is not set
    '''
    leg_count=18
    response=client.get("/get_count", params={'leg_count':leg_count})
    assert response.status_code==422

def test_5_get_count():
    '''
    When heads and legs are available and do not yield a success
    '''
    head_count=7
    leg_count=17
    response= client.get("/get_count", params={'head_count':head_count, 'leg_count':leg_count})
    assert response.status_code==400
