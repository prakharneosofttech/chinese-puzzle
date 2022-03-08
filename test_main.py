from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_1_get_count():
    head_count=10
    leg_count=22
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)

def test_2_get_count():
    head_count=10
    leg_count=20
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)

def test_3_get_count():
    head_count=9
    leg_count=19
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)

def test_4_get_count():
    head_count=8
    leg_count=18
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)

def test_5_get_count():
    head_count=7
    leg_count=17
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)

def test_6_get_count():
    head_count=6
    leg_count=16
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)
def test_7_get_count():
    head_count=5
    leg_count=15
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)

def test_8_get_count():
    head_count=5
    leg_count=14
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)
    
def test_9_get_count():
    head_count=5
    leg_count=13
    response=client.get("/get_count")
    assert response.status_code==200
    assert head_count<=leg_count
    assert leg_count%2==0
    assert (leg_count//2 >= head_count)
