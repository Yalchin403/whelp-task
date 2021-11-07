import requests


response = requests.post(
            "http://localhost:5000/api/v1/task",
            json={
                "address": "180.71.104.224"
            }
        )
task_id = response.json()["task_id"]
    
def test_check_status():
    response = requests.get(
            f"http://localhost:5000/api/v1/status/{task_id}",
        )

    assert response.status_code == 200
