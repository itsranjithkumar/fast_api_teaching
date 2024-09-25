from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import employee, leave


app = FastAPI()


origins = [
    "http://localhost:5173",  # Your frontend origin
    "http://127.0.0.1:5173",  # Alternative frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(employee.router)
app.include_router(leave.router)

