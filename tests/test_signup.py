import requests


def test_signup():
    response = requests.post(
        "http://localhost:5000/api/v1/signup",
        json={
            "age": 21,
            "name": "Yalchin",
            "surname": "Mammadli",
            "username": "Yalchin405",
            "email": "yalchinmammadli@yalchin.info",
            "gender": "M",
            "password": "Yalcin-1"
        }
    )
    
    assert response.status_code == 200 or response.status_code == 409
