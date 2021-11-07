from celery import Celery
import dotenv
import os



dotenv.load_dotenv()
IP_API_KEY = os.getenv("IP_API_KEY")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery.task
def get_ip_details(ip):
    from ipdata import ipdata
    ipdata =  ipdata.IPData(IP_API_KEY)
    response = ipdata.lookup(ip)

    return response
