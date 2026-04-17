from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/teste_async")
async def teste(id: int):
    await asyncio.sleep(1)
    return "Teste " + str(id)
