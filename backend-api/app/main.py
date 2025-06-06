from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/sayHello")
def say_hello():
    return JSONResponse(content={"message": "Hello User"})
