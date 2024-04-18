# test_chess_event_api.py

import pytest
import requests

@pytest.fixture
def api_url():
    return "http://192.168.1.26:8000/events"

def test_get_chess_events_returns_200(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200

def test_get_chess_events_returns_list_of_events(api_url):
    response = requests.get(api_url)
    assert isinstance(response.json(), list)
    assert all("event_name" in event for event in response.json())

def test_event_structure(api_url):
    response = requests.get(api_url)
    events = response.json()
    assert all(
        {"event_name", "start_date", "end_date"} <= set(event.keys()) for event in events
    )

def test_event_content(api_url):
    response = requests.get(api_url)
    events = response.json()
    assert any(event["event_name"] == "Chess Championship" for event in events)

def test_empty_database(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_error_handling(api_url):
    # Assuming an invalid database connection
    response = requests.get(api_url)
    assert response.status_code == 500

def test_unauthorized_access(api_url):
    # Assuming access without proper authentication
    response = requests.get(api_url)
    assert response.status_code == 401

