from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.routes import router

app = FastAPI()

origins = [
    "*", # @TODO: if you are planning integrate this code with frontend then add the urls and remove '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix='/api')

@app.get("/")
async def main():
    return {"response":"AI Agent Started"}