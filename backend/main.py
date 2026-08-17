from fastapi import FastAPI
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str
    technologies: list[str]

app = FastAPI()

all_projects =[]

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.post("/projects")
def add_project(project: ProjectCreate):
    all_projects.append(project)
    return project

@app.get("/projects")
def full_projects():
    return all_projects


    