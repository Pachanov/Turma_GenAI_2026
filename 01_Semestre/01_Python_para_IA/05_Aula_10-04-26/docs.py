from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/verificar-cpf/{cpf_teste}")
def verificar_cpf(
    cpf_teste: Annotated[int, Path(title="CPF", description="O CPF a ser testado", ge=1, le=99999999999)]
):
    return {"valido": True}
