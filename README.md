# 🖥️ API de Chamados de TI

> Sistema de gestão de chamados técnicos desenvolvido com **Python + FastAPI + PostgreSQL**

---

## 📌 Sobre o Projeto

API REST para gerenciamento de chamados de suporte técnico. Permite que times de TI registrem, acompanhem e resolvam problemas técnicos de forma organizada, com controle de prioridade, status e responsável por cada chamado.

Desenvolvido com **FastAPI**, framework Python moderno adotado por empresas como Netflix, Uber e Microsoft, com persistência de dados em **PostgreSQL** e dashboard frontend em HTML puro.

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|---|---|---|
| Python | 3.13+ | Linguagem principal |
| FastAPI | 0.135+ | Framework da API |
| Uvicorn | 0.44+ | Servidor ASGI assíncrono |
| SQLAlchemy | 2.0+ | ORM para o banco de dados |
| PostgreSQL | 18+ | Banco de dados relacional |
| Pydantic | 2.0+ | Validação de dados |
| python-dotenv | 1.2+ | Gerenciamento de variáveis de ambiente |
| HTML + CSS + JS | — | Dashboard frontend |

---

## 📁 Estrutura do Projeto

```
backend-chamados/
│
├── models/
│   └── chamado.py        # Define a tabela no banco de dados
│
├── routers/
│   └── chamados.py       # Rotas do CRUD (GET, POST, PUT, DELETE)
│
├── schemas/
│   └── chamado.py        # Validação e serialização dos dados
│
├── database.py           # Conexão com o PostgreSQL
├── main.py               # Inicialização da API
├── frontend.html         # Dashboard visual do sistema
├── .env                  # Variáveis de ambiente (não versionar)
└── requirements.txt      # Dependências do projeto
```

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos

- [Python 3.13+](https://www.python.org/downloads/)
- [PostgreSQL 18+](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)

---

### 1. Clone o repositório

```bash
git clone https://github.com/EduardoBelorio/backend-chamados.git
cd backend-chamados
```

### 2. Crie e ative o ambiente virtual

```bash
# Criar
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv
```

### 4. Configure o banco de dados

Crie um banco chamado `chamados` no PostgreSQL, depois crie o arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://postgres:sua_senha@localhost:5432/chamados
```

> ⚠️ Substitua `sua_senha` pela senha do seu PostgreSQL.

### 5. Suba a API

```bash
uvicorn main:app --reload
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Abra o dashboard

Com a API rodando, abra o arquivo `frontend.html` diretamente no navegador. O dashboard conecta automaticamente na API.

---

## 📖 Documentação Interativa

O FastAPI gera automaticamente duas interfaces de documentação — sem nenhuma configuração extra:

| Interface | URL |
|---|---|
| Swagger UI | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| ReDoc | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |

---

## 🔁 Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/chamados/` | Criar novo chamado |
| `GET` | `/chamados/` | Listar todos os chamados |
| `GET` | `/chamados/{id}` | Buscar chamado por ID |
| `PUT` | `/chamados/{id}` | Atualizar chamado |
| `DELETE` | `/chamados/{id}` | Deletar chamado |

---

## 📋 Exemplos de Uso

### Criar um chamado — `POST /chamados/`

```json
{
  "titulo": "Computador não liga",
  "descricao": "O computador da sala 3 não está ligando desde segunda-feira",
  "prioridade": "alta",
  "responsavel": "João Silva"
}
```

**Resposta:**
```json
{
  "id": 1,
  "titulo": "Computador não liga",
  "descricao": "O computador da sala 3 não está ligando desde segunda-feira",
  "prioridade": "alta",
  "status": "aberto",
  "responsavel": "João Silva",
  "criado_em": "2026-04-14T09:58:33.946802",
  "atualizado_em": null
}
```

### Atualizar status — `PUT /chamados/1`

```json
{
  "status": "em_andamento"
}
```

### Deletar — `DELETE /chamados/1`

```json
{
  "mensagem": "Chamado deletado com sucesso"
}
```

---

## 🗄️ Modelo do Banco de Dados

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer (PK) | Identificador único gerado automaticamente |
| `titulo` | String(200) | Título do chamado |
| `descricao` | String(1000) | Descrição detalhada do problema |
| `prioridade` | String(50) | `baixa`, `media` ou `alta` |
| `status` | String(50) | `aberto`, `em_andamento` ou `resolvido` |
| `responsavel` | String(100) | Nome do responsável pelo chamado |
| `criado_em` | DateTime | Preenchido automaticamente na criação |
| `atualizado_em` | DateTime | Atualizado automaticamente a cada edição |

---

## 🎨 Dashboard

O projeto inclui um dashboard frontend em HTML puro que conecta diretamente na API, sem necessidade de frameworks adicionais. Funcionalidades:

- Cards de métricas em tempo real (total, abertos, em andamento, resolvidos)
- Formulário para criar novos chamados
- Tabela completa com badges de prioridade e status
- Botões de resolver e excluir diretamente na tabela

---

## 📚 Referências

- [Documentação oficial FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Pydantic Docs](https://docs.pydantic.dev/)
