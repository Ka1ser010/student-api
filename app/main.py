

from fastapi import FastAPI
from app.database import Base, engine
from app.routers import students

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="School - Students manager",
    description="API REST to manage students.",
    version="0.1.0",
)

app.include_router(students.router)


@app.get("/")
def root():
    return {"message": "API running. Access /docs for the interactive documentation."}
