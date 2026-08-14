from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Task(BaseModel):
    id: int
    title: str


app = FastAPI(title="Task Manager API", version="0.1.0")

_TASKS: tuple[Task, ...] = (Task(id=1, title="Первая задача"),)


@app.get("/", response_model=Message)
def root() -> Message:
    return Message(message="API работает")


@app.get("/tasks", response_model=list[Task])
def get_tasks() -> list[Task]:
    return list(_TASKS)
