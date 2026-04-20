# Arquivo principal que inicializa a API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import chamados

# Cria todas as tabelas no banco automaticamente
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação
app = FastAPI(
    title="API de Chamados de TI",
    description="Sistema de gestão de chamados técnicos — Programação Web II",
    version="1.0.0"
)

# Permite que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(chamados.router)

# Rota de teste
@app.get("/")
def inicio():
    return {"mensagem": "API de Chamados de TI rodando com sucesso! 🚀"}