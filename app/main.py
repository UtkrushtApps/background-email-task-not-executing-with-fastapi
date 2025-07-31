from fastapi import FastAPI, Depends
from app.schemas import UserCreate
from app.database import get_async_session
from fastapi import BackgroundTasks

app = FastAPI()

@app.post("/register")
async def register_user(user: UserCreate, background_tasks: BackgroundTasks, session=Depends(get_async_session)):
    pass
