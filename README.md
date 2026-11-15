# Constituição Simples

**A Constituição brasileira em uma linguagem que todo mundo entende.**

O **Constituição Simples** é um projeto open source que busca tornar a Constituição Federal de 1988 mais acessível, compreensível e próxima da realidade das pessoas.

A plataforma permitirá consultar o texto constitucional original, compreender dispositivos jurídicos por meio de explicações em linguagem simples e explorar exemplos de situações do cotidiano.

O objetivo é contribuir para a democratização do acesso à informação jurídica, aproximando os cidadãos de seus direitos e deveres.

## Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-149ECA?style=for-the-badge&logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-412991?style=for-the-badge&logo=openai&logoColor=white)

**Outras ferramentas:** Alembic, HTTPX, Pydantic, Pytest, Ruff e Git.

## Funcionalidades previstas

- **Constituição completa:** acesso ao texto original da Constituição Federal.
- **Linguagem simples:** explicações acessíveis de artigos e dispositivos constitucionais.
- **Exemplos cotidianos:** situações práticas que ajudam a compreender direitos e deveres.
- **Glossário jurídico:** definições de termos jurídicos complexos.
- **Busca inteligente por assunto:** localização de conteúdos por tema ou número do artigo.
- **Comparação de textos:** visualização do dispositivo original e sua explicação simplificada.
- **Acessibilidade:** experiência responsiva, com prioridade para dispositivos móveis.

## Como funciona a inteligência artificial?

A IA será utilizada durante a preparação do conteúdo, e não durante a navegação dos usuários.

O processo previsto consiste em:

1. Obter o texto oficial da Constituição Federal.
2. Organizar artigos e dispositivos em uma estrutura consultável.
3. Gerar explicações simplificadas, exemplos e definições por meio de modelos de linguagem.
4. Realizar verificações automáticas e uma avaliação adicional do conteúdo gerado.
5. Armazenar as explicações aprovadas para publicação no PostgreSQL.
6. Disponibilizar os conteúdos na plataforma sem depender de chamadas à IA a cada acesso.

O texto constitucional original será preservado e apresentado separadamente das explicações.

**Importante:** as explicações produzidas por IA terão caráter educativo e informativo. As verificações automatizadas não equivalem à revisão jurídica profissional, e a plataforma não substituirá orientação jurídica especializada.

## Estrutura do projeto

```text
constituicao-simples/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   └── config.py
│   │   └── db/
│   │       ├── __init__.py
│   │       ├── base.py
│   │       └── session.py
│   ├── scripts/
│   │   └── test_openrouter.py
│   ├── alembic/
│   │   ├── versions/
│   │   ├── env.py
│   │   └── script.py.mako
│   ├── alembic.ini
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── .env.example
│   └── .env
├── frontend/
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

*Estrutura baseada na configuração inicial do EP-01. Os módulos de API, modelos, importação constitucional e geração de conteúdo serão adicionados conforme o desenvolvimento.*

### Backend

Responsável pela API REST, integração com o PostgreSQL, processamento do texto constitucional e preparação das explicações por inteligência artificial.

### Frontend

Interface web construída com React e TypeScript, priorizando navegação intuitiva, acessibilidade e experiência Mobile First.

### Banco de dados

O PostgreSQL armazenará o texto constitucional estruturado, explicações, glossário e associações temáticas.

O SQLAlchemy será utilizado para acesso aos dados, enquanto o Alembic controlará as alterações na estrutura do banco.

### Infraestrutura

O Docker Compose permitirá reproduzir o ambiente de desenvolvimento em Windows e Linux, inicialmente com o PostgreSQL.

## Estado do desenvolvimento

**EP-01 — Configuração inicial da infraestrutura (em andamento)**

- [x] Preparação do ambiente Python.
- [x] Configuração das variáveis de ambiente.
- [x] Integração inicial com OpenRouter.
- [x] Preparação do Docker Compose.
- [x] Configuração inicial do SQLAlchemy.
- [x] Inicialização do Alembic.
- [ ] Validação da conexão com PostgreSQL.
- [ ] Modelagem das tabelas iniciais.
- [ ] Primeiras migrações do banco.
- [ ] Implementação dos endpoints da API.
- [ ] Desenvolvimento da interface web.

## Licença

A licença de código aberto será definida antes da primeira versão pública.

---

**Constituição Simples — Conhecer seus direitos não deveria ser complicado.**
