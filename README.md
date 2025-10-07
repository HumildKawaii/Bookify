# 📚 Bookify
O Bookify é uma API simples e intuitiva para gerenciar uma coleção de livros.
Com ela, é possível criar, listar, atualizar e deletar livros usando requisições HTTP (CRUD completo).
Desenvolvido com FastAPI, SQLAlchemy e SQLite.

# 🚀 Funcionalidades

✅ Criar novos livros
✅ Listar todos os livros ou filtrar por autor, gênero ou ano
✅ Buscar livro por ID
✅ Atualizar informações de um livro existente
✅ Deletar um livro
✅ Banco de dados SQLite integrado

# 🧰 Tecnologias usadas

Python 3.14+

FastAPI

Uvicorn

SQLAlchemy

Pydantic

# Instalação e uso
´´´Clonar o repositório
git clone https://github.com/HumildKawaii/Bookify.git
cd Bookify´´´

# Instalar dependências
´´´pip install -r requirements.txt´´´

# Rodar o servidor local
uvicorn app.main:app --reload

# Acessar no navegador:

👉 http://127.0.0.1:8000
Você verá:
{"Lucas": "Bem-vindo à API de livros!"}

# Testar os endpoints

Abra a documentação interativa da API gerada automaticamente pelo FastAPI:
Swagger UI: http://127.0.0.1:8000/docs
