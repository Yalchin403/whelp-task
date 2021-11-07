import requests


response = requests.post(
        "http://localhost:5000/api/v1/auth",
        json={
            "username": "Yalchin405",
            "password": "Yalcin-1"
        }
    )

access_token=response.json()["access_token"]
header = {'Authorization': 'Bearer ' + access_token}

def test_user():
    response = requests.get("http://localhost:5000/user", headers=header)
    assert response.status_code == 200

test_user()