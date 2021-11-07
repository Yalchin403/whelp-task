import dotenv
import os
from fastapi import APIRouter
from auth.auth import AuthHandler
from worker_task import get_ip_details
from worker_task import celery as app
from schemas.task import Ip
from models.ip_details import IpDetail
from celery.result import AsyncResult

task = APIRouter()
auth_handler = AuthHandler()

dotenv.load_dotenv()
IP_API_KEY = os.getenv('IP_API_KEY')

@task.get("/api/v1/status/{id}")
async def check_task_status(id:str):
    result = AsyncResult(id, app=app)
    return {"status": result.state}


@task.post("/api/v1/task")
async def create_task(ip: Ip):
    # before creating a task we can check if we already got the details in our db
    # but honestly i was lazy to do that as this project is only for testing purposes
    task = get_ip_details.delay(ip.address)
    result = task.get()
    ip_detail_obj = IpDetail(
        ip=ip.address,
        details=result
    )
    ip_detail_obj.save()
    
    return {"task_id": task.id}
