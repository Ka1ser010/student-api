# ACQUA_ENCANTO — Gerenciador de Alunos (API REST)

## Stack (Fase 1)

- **FastAPI** — framework web
- **SQLAlchemy** — ORM (mapeamento objeto-relacional)
- **SQLite** — banco de dados local (arquivo único, sem instalação)
- **Pytest** — testes automatizados

## Como rodar

```bash
# 1. Criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Subir o servidor
uvicorn app.main:app --reload
```

A API sobe em `http://127.0.0.1:8000`. A documentação interativa
(Swagger, gerada automaticamente pelo FastAPI) fica em
`http://127.0.0.1:8000/docs` — dá pra testar todas as rotas direto
pelo navegador, sem precisar de Postman.

## Rodar os testes

```bash
pytest -v
```

## Endpoints disponíveis

| Método | Rota                | Descrição                        |
|--------|----------------------|-----------------------------------|
| POST   | `/students/`         | Cria um novo aluno                |
| GET    | `/students/`         | Lista alunos (com paginação)      |
| GET    | `/students/{id}`     | Busca um aluno específico         |
| PUT    | `/students/{id}`     | Atualiza um ou mais campos        |
| DELETE | `/students/{id}`     | Remove um aluno                   |

## Estrutura do projeto

```
app/
├── main.py            # inicializa o FastAPI e registra as rotas
├── database.py         # conexão com o banco (SQLite por enquanto)
├── models.py            # tabelas (SQLAlchemy)
├── schemas.py           # validação de entrada/saída (Pydantic)
└── routers/
    └── students.py       # rotas CRUD de alunos
tests/
└── test_students.py      # testes automatizados do CRUD
```

## Roadmap (próximas fases)

- [x] **Fase 1** — CRUD básico sem autenticação, SQLite
- [ ] **Fase 2** — Trocar SQLite por PostgreSQL + Docker Compose
- [ ] **Fase 3** — Autenticação JWT (registro/login, rotas protegidas)
- [ ] **Fase 4** — Paginação avançada, filtros de busca por nome/nível
- [ ] **Fase 5** — Deploy (ex: Railway, Render ou Fly.io)

## Por que esse projeto existe

Construído como parte de um portfólio de backend, aplicando conceitos de
API REST, ORM e testes automatizados a um problema real de gestão de
alunos de uma escola de natação.
