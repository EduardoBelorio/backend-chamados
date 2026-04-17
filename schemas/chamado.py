# Define como os dados entram e saem da API
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Dados obrigatórios para CRIAR um chamado
class ChamadoCreate(BaseModel):
    titulo: str
    descricao: str
    prioridade: str  # baixa, media, alta
    responsavel: str

# Dados para ATUALIZAR um chamado (todos opcionais)
class ChamadoUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    prioridade: Optional[str] = None
    status: Optional[str] = None
    responsavel: Optional[str] = None

# Como o chamado aparece na resposta da API
class ChamadoResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str
    responsavel: str
    criado_em: datetime
    atualizado_em: Optional[datetime] = None

    class Config:
        from_attributes = True