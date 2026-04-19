from fastapi import FastAPI

import services
from schema import UserIn, BaseResponse, UserListOut
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Hello from FastAPI ;)"}


@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    """
    Add user data to json file
    """
    try:
        services.add_userdata(user.dict())
    except Exception:
        return {"success": False}
    return {"success": True}


@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from json file
    """
    return services.read_usersdata()


# Prometheus metrics
Instrumentator().instrument(app).expose(app)
