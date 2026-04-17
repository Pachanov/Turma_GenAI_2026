from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/saudacao")
def saudacao():
    return {"saudacao": "Olá Mundo!"}

@app.get("/hora_atual")
def hora_atual():
    return {"hora": str(datetime.datetime.now())}
