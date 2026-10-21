# cd ~/Server-Dashboard
# source .venv/bin/activate
# python3 -m uvicorn back_end.main:app --host 0.0.0.0 --port 8000

#rsync -av --exclude='.venv' --exclude='.git' --exclude='__pycache__' ./ urmango@10.0.0.252:~/Server-Dashboard/

# http://127.0.0.1:8000/

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from back_end.services import get_all_services
import back_end.monitor as monitor


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/hello")
def say_hello():
    return {"message": "Hello"}

@app.get("/services")
def get_services_status():
    return {"message": get_all_services()}

@app.get("/monitor")
def get_monitoring():
    return {
    "cpu": monitor.get_cpu_usage(),
    "ram": monitor.get_memory_usage(),
    "up_time": monitor.get_uptime(),
    "storage": monitor.get_storage_usage(),
    "temp": monitor.get_temp()
 }

