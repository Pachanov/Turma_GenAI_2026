from fastapi import FastAPI
app = FastAPI()

@app.get("/verificar-cpf/{cpf_teste}")
def verificar_cpf(cpf_teste: int):
    return True
