import requests


auth_token='kbkcmbkcmbkcbc9ic9vixc9vixc9v'
hed = {'Authorization': 'Bearer ' + auth_token}

def test_auth():
    response = requests.post(
        "http://localhost:5000/api/v1/refresh",
        json={
            "username": "Yalchin405",
            "password": "Yalcin-1"
        }
    )

    assert response.status_code == 200
