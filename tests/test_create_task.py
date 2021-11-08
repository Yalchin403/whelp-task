import requests


def test_create_task():
    # we can also mock the third part API, for us not to be dependent on that API
    response = requests.post(
            "http://localhost:5000/api/v1/task",
            json={
                "address": "180.71.104.224"
            }
        )

    assert response.status_code == 200
