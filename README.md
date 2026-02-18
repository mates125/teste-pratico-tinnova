# Controle de Veículos – API
Projeto desenvolvido como parte do desafio técnico para o processo seletivo para a vaga de Desenvolvedor Python Pleno na Tinnova. 

A aplicação consiste em uma API REST para gerenciamento de veículos, protegida por autenticação JWT, e um frontend simples em Django para facilitar a validação da solução.


## Visão geral

Funcionalidades implementadas:

- Autenticação via JWT
- Perfis de usuário (ADMIN e USER)
- CRUD completo de veículos
- Soft delete
- Filtros de busca
- Relatório de veículos por marca
- Cache (Redis)
- Testes automatizados com pytest
- Frontend funcional para consumo da API

---

## Tecnologias utilizadas

- Python 3.12
- Django
- Django REST Framework
- SimpleJWT
- Pytest
- SQLite (desenvolvimento)
- Redis (cache)
- HTML + Django Templates

---

## Estrutura do projeto

├── controle_veiculos/ # API (regras de negócio)
├── frontend/ # Frontend Django
├── core/ # Configurações do projeto
├── manage.py
├── requirements.txt
├── requirements-dev.txt
└── README.md

---

## Como rodar o projeto localmente

### 1. Clonar o repositório
```
git clone https://github.com/mates125/teste-pratico-tinnova.git
cd teste-pratico-tinnova
```

### 2. Criar e ativar o ambiente virtual
```
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```
pip install -r requirements-dev.txt
```

### 4. Rodar as migrations
```
python manage.py migrate
```

### 5. Criar um usuário administrador
```
python manage.py createsuperuser
```
- Username: admin
- Email: admin@admin.com
- Password: 123

### 6. Criar um usuário padrão
```
python manage.py shell
```
Colar no shell:

```
from django.contrib.auth.models import User
User.objects.create_user(username="user", password="123")
```


### 7. Iniciar o Docker que contém o Redis
```
docker compose up -d
```

### 8. Iniciar o servidor
```
python manage.py runserver
```

A aplicação ficará disponível em:

http://127.0.0.1:8000


## Autenticação (JWT)
A autenticação da API é feita via JWT.

### Obter token

POST<br>http://127.0.0.1:8000/api/token/

### Body (JSON):
```
{
  "username": "admin",
  "password": "123"
}
```

### Resposta:
```
{
  "access": "<token>",
  "refresh": "<token>"
}
```

O token deve ser enviado no header:<br>
Authorization: Bearer {token}

## Perfis de usuário

### ADMIN

- Criar veículos
- Atualizar veículos
- Remover veículos (soft delete)
- Listar e filtrar
- Acessar relatórios

### USER

- Listar veículos
- Filtrar veículos
- Visualizar detalhes
- Não pode criar, editar ou remover

## Endpoints da API

### Listagem de veículos

GET /api/veiculos/

### Exemplos de filtros disponíveis
/api/veiculos?marca=Ford
/api/veiculos?modelo=Ka
/api/veiculos?placa=ABC
/api/veiculos?ano=2020
/api/veiculos?cor=Preto
/api/veiculos?minPreco=9000&maxPreco=15000
/api/veiculos?id=1

### Detalhes do veículo
GET <br>/api/veiculos/{id}/

### Criar veículo (ADMIN)
POST <br>/api/veiculos/

### Atualizar veículo (ADMIN)
PUT <br>/api/veiculos/{id}/

PATCH <br>/api/veiculos/{id}/

### Remover veículo (ADMIN – soft delete)
DELETE <br>/api/veiculos/{id}/

### Relatório por marca
GET<br> /api/veiculos/relatorios/por-marca/

## Frontend
O frontend foi incluído para facilitar a validação da solução.

### Funcionalidades
- Login
- Listagem de veículos
- Filtros de busca
- Detalhe do veículo
- Criação, edição e exclusão (ADMIN)
- Logout

### Rotas principais
/           → redireciona para login<br>
/login      → login<br>
/veiculos   → listagem e filtros

## Testes automatizados

Os testes foram desenvolvidos com pytest e cobrem:

- Autenticação
- Permissões
- CRUD
- Filtros
- Relatórios
- Cache

## Rodar os testes
```
pytest
```

Warnings podem aparecer devido a dependências, mas não afetam o funcionamento do projeto.

### Banco de dados

O arquivo db.sqlite3 não é versionado e é criado automaticamente ao rodar as migrations
```
python manage.py migrate
```