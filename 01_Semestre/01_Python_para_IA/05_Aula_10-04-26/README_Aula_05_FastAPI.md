# Aula 05 — FastAPI e Consumo de APIs

Este pacote reúne os arquivos recriados da aula sobre consumo de APIs, FastAPI, parâmetros, documentação automática, métodos HTTP, tratamento de exceções e `async`.

## Requisitos

Ative o ambiente antes de executar os exemplos:

```powershell
conda activate ambiente
```

Instale as dependências, se necessário:

```powershell
pip install fastapi "fastapi[standard]" requests
```

---

## Estrutura dos arquivos

### `consumidor.py`
Consome a API Open-Meteo:
- busca latitude e longitude de uma cidade
- consulta a temperatura atual

Executar:

```powershell
python consumidor.py
```

---

### `servidor.py`
API básica com duas rotas:
- `/saudacao`
- `/hora_atual`

Executar:

```powershell
fastapi dev servidor.py
```

Testar:
- `http://127.0.0.1:8000/saudacao`
- `http://127.0.0.1:8000/hora_atual`
- `http://127.0.0.1:8000/docs`

---

### `parametros.py`
Exemplo de uso de parâmetro de rota (`Path Param`):
- `/verificar-cpf/{cpf_teste}`

Executar:

```powershell
fastapi dev parametros.py
```

Testar:
- `http://127.0.0.1:8000/verificar-cpf/12345678909`

---

### `docs.py`
Exemplo com documentação enriquecida usando:
- `Annotated`
- `Path`
- título
- descrição
- limites de valor

Executar:

```powershell
fastapi dev docs.py
```

Testar:
- `http://127.0.0.1:8000/docs`

---

### `metodos.py`
Exemplo de métodos HTTP:
- `POST /adicionar-pessoa`
- `GET /nome-pessoa/{cpf}`
- `PUT /atualizar-pessoa`

Executar:

```powershell
fastapi dev metodos.py
```

Testar em:
- `http://127.0.0.1:8000/docs`

---

### `http_exception_api.py`
Exemplo de tratamento de erros com:
- `HTTPException`

Executar:

```powershell
fastapi dev http_exception_api.py
```

Testar em:
- `http://127.0.0.1:8000/docs`

---

### `async_api.py`
Exemplo de rota assíncrona:
- `GET /teste_async`

Executar:

```powershell
fastapi dev async_api.py
```

Testar:
- `http://127.0.0.1:8000/teste_async?id=1`

---

### `cliente_async.py`
Cliente para testar concorrência com threads.
Ele dispara 100 requisições para a rota `/teste_async`.

Executar com o servidor `async_api.py` já em execução:

```powershell
python cliente_async.py
```

---

## Observações importantes

- Rode apenas **um servidor FastAPI por vez** na porta `8000`.
- Sempre use o modo de desenvolvimento durante os testes:

```powershell
fastapi dev nome_do_arquivo.py
```

- A documentação automática fica disponível em:

```text
http://127.0.0.1:8000/docs
```

- Os serviços estão acessíveis apenas localmente em:

```text
127.0.0.1
```

Isso é mais seguro durante o desenvolvimento.

---

## Sugestão de fluxo de estudo

1. Execute `consumidor.py`
2. Rode `servidor.py`
3. Teste `parametros.py`
4. Teste `docs.py`
5. Teste `metodos.py`
6. Teste `http_exception_api.py`
7. Rode `async_api.py`
8. Execute `cliente_async.py`

---

## Versionamento

Depois de restaurar os arquivos no seu projeto, salve no Git:

```powershell
git add .
git commit -m "Restaura arquivos da aula de FastAPI"
git push
```
