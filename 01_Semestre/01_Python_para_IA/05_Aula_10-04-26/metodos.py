from fastapi import FastAPI
app = FastAPI()
dict_pessoas = {}

@app.post("/adicionar-pessoa")
def adicionar_pessoa(cpf: int, nome: str):
    dict_pessoas[cpf] = (cpf, nome)
    return {"mensagem": "Pessoa adicionada com sucesso"}

@app.get("/nome-pessoa/{cpf}")
def nome_pessoa(cpf: int):
    return {"nome": dict_pessoas[cpf][1]}

@app.put("/atualizar-pessoa")
def atualizar_pessoa(cpf: int, nome: str):
    dict_pessoas[cpf] = (cpf, nome)
    return {"mensagem": "Pessoa atualizada com sucesso"}
