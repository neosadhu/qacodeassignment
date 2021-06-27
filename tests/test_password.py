import pytest
import requests


#SOME AUTOMATED TESTS

url = "http://127.0.0.1:8088"
headers = {'Content-Type': 'application/json'}

def test_send_a_valid_post():
    payload = "{\"password\": \"angrymonkey\"}"
    response = requests.request("POST", url +"/hash", headers=headers, data=payload)
    assert response.status_code == 200
    assert len(response.text)>0;

def test_send_an_invalid_post_empty_string():
    payload = "{""}"
    response = requests.request("POST", url +"/hash", headers=headers, data=payload)
    assert response.status_code == 400
    assert len(response.text)==0;

def test_send_an_invalid_post_invalid_string():
    payload = "{\"test123\": \"invalid\"}"
    response = requests.request("POST", url +"/hash", headers=headers, data=payload)
    assert response.status_code ==400
    assert len(response.text)==0;

def test_request_to_invalid_port_number():
    url = "http://127.0.0.1:8089"
    payload = "{\"test123\": \"invalid\"}"
    with pytest.raises(Exception):
        response = requests.request("POST", url + "/hash", headers=headers, data=payload)

def test_request_to_stats_returns_valid_json():
    response = requests.request("GET", url +"/stats", headers=headers)
    assert response.status_code == 200
    assert "TotalRequests" in response.json()
    assert "AverageTime" in response.json()
    assert (type(response.json()["AverageTime"])) == int;
    assert (type(response.json()["TotalRequests"]))== int;

def test_invalid_request_to_stats_returns_a_400():
    response = requests.request("GET", url +"/stats?key1=key1&key2=key2", headers=headers)
    assert response.status_code == 400
    assert "TotalRequests" in response.json()
    assert "AverageTime" in response.json()
    assert (type(response.json()["AverageTime"])) == int;
    assert (type(response.json()["TotalRequests"]))== int;


def test_shutdown_the_application():
    response = requests.request(method = "POST", url = url +"/hash" , data = "shutdown",  headers = headers)
    assert response.status_code == 200;

    with pytest.raises(Exception):
        #try the request again
        payload = "{\"password\": \"angrymonkey\"}"
        response = requests.request("POST", url +"/hash", headers=headers, data=payload)
        assert response.status_code !=200

