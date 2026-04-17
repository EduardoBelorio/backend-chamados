# Define todas as rotas da API de chamados
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.chamado import Chamado
from schemas.chamado import ChamadoCreate, ChamadoUpdate, ChamadoResponse
from typing import List

router = APIRouter(prefix="/chamados", tags=["Chamados"])

# CREATE - Criar novo chamado
@router.post("/", response_model=ChamadoResponse)
def criar_chamado(chamado: ChamadoCreate, db: Session = Depends(get_db)):
    novo = Chamado(**chamado.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# READ - Listar todos os chamados
@router.get("/", response_model=List[ChamadoResponse])
def listar_chamados(db: Session = Depends(get_db)):
    return db.query(Chamado).all()

# READ - Buscar chamado por ID
@router.get("/{id}", response_model=ChamadoResponse)
def buscar_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.query(Chamado).filter(Chamado.id == id).first()
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    return chamado

# UPDATE - Atualizar chamado
@router.put("/{id}", response_model=ChamadoResponse)
def atualizar_chamado(id: int, dados: ChamadoUpdate, db: Session = Depends(get_db)):
    chamado = db.query(Chamado).filter(Chamado.id == id).first()
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(chamado, campo, valor)
    db.commit()
    db.refresh(chamado)
    return chamado

# DELETE - Remover chamado
@router.delete("/{id}")
def deletar_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.query(Chamado).filter(Chamado.id == id).first()
    if not chamado:
        raise HTTPException(status_code=404, detail="Chamado não encontrado")
    db.delete(chamado)
    db.commit()
    return {"mensagem": "Chamado deletado com sucesso"}