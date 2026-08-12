cat << 'EOF' > README.md
# 🚀 API REST com FastAPI, PostgreSQL & Docker Compose

Uma API REST assíncrona desenvolvida em Python (FastAPI) e integrada ao PostgreSQL, com orquestração completa em containers Docker e pipeline de CI/CD automatizada via GitHub Actions.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Framework:** FastAPI / Uvicorn
- **Banco de Dados:** PostgreSQL 16
- **Containerização:** Docker & Docker Compose
- **CI/CD:** GitHub Actions

## ⚙️ Funcionalidades

- CRUD básico de produtos (criação e listagem)
- Conexão resiliente com o banco de dados via driver `psycopg2`
- Mapeamento de volume Docker para persistência de dados do PostgreSQL
- Documentação interativa Swagger/OpenAPI integrada
- Teste automatizado de build de infraestrutura na pipeline de CI

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Docker e Docker Compose instalados.

### Passo a passo

1. Clone este repositório:
git clone https://github.com/MarlonDeam/api-devops-postgres.git
cd api-devops-postgres

2. Suba a aplicação e o banco de dados:
docker compose up --build

3. Acesse a documentação no navegador:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 📌 Rotas da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | / | Healthcheck da API |
| GET | /produtos | Retorna a lista de produtos cadastrados |
| POST | /produtos | Cadastra um novo produto |

## 🔄 Pipeline de CI/CD

O repositório conta com um workflow do GitHub Actions (`.github/workflows/ci.yml`) disparado a cada push na branch `main` para validar a construção dos containers.
EOF

