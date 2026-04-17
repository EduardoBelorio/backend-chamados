# Define a tabela de chamados no banco de dados
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descricao = Column(String(1000), nullable=False)
    prioridade = Column(String(50), nullable=False)  # baixa, media, alta
    status = Column(String(50), default="aberto")    # aberto, em_andamento, resolvido
    responsavel = Column(String(100), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())
    atualizado_em = Column(DateTime, onupdate=func.now())