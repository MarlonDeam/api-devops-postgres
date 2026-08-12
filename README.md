# 🚀 API REST com FastAPI, PostgreSQL & Docker Compose

Uma API REST assíncrona desenvolvida em Python (FastAPI) e integrada ao PostgreSQL, com orquestração completa em containers Docker e pipeline de CI/CD automatizada via GitHub Actions.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Framework:** FastAPI / Uvicorn
* **Banco de Dados:** PostgreSQL 16
* **Containerização:** Docker & Docker Compose
* **CI/CD:** GitHub Actions

---

## ⚙️ Funcionalidades

- [x] CRUD básico de produtos (criação e listagem).
- [x] Conexão resiliente com o banco de dados via driver `psycopg2`.
- [x] Mapeamento de volume Docker para persistência de dados do PostgreSQL.
- [x] Documentação interativa Swagger/OpenAPI integrada.
- [x] Teste automatizado de build de infraestrutura na pipeline de CI.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.

### Passo a passo

1. Clone este repositório:
   ```bash
   git clone [https://github.com/MarlonDeam/api-devops-postgres.git](https://github.com/MarlonDeam/api-devops-postgres.git)
   cd api-devops-postgres
Suba a aplicação e o banco de dados com um único comando:Bashdocker compose up --build
Acesse a documentação interativa no seu navegador:Swagger UI: http://localhost:8000/docsReDoc: http://localhost:8000/redoc📌 Rotas da APIMétodoRotaDescriçãoGET/Healthcheck da APIGET/produtosRetorna a lista de produtos cadastradosPOST/produtosCadastra um novo produto🔄 Pipeline de CI/CDO repositório conta com um workflow do GitHub Actions (.github/workflows/ci.yml) que é disparado a cada push na branch main. Ele realiza o build dos containers em um ambiente isolado para garantir a integridade da aplicação antes de qualquer alteração ir para produção.
---

### Para subir o README para o GitHub:

```bash
git add README.md
git commit -m "docs: adiciona README com instrucoes do projeto"
git push origin main

