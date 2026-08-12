import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Produtos - DevOps")

class Produto(BaseModel):
    nome: str
    preco: float

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:10452003@db:5432/produtos_db")

def get_db_connection():
    """Tenta conectar ao PostgreSQL com retry para aguardar o banco subir"""
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("Não foi possível conectar ao banco de dados.")

def init_db():
    """Cria a tabela no banco de dados se ela ainda não existir"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco DECIMAL(10, 2) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_db()

@app.get("/")
def home():
    return {"status": "API rodando com sucesso!", "banco": "PostgreSQL Conectado"}

@app.get("/produtos")
def listar_produtos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos;")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return produtos

@app.post("/produtos", status_code=201)
def criar_produto(produto: Produto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s) RETURNING *;",
        (produto.nome, produto.preco)
    )
    novo_produto = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return novo_produto
