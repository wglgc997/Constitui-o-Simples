# Constituição Simples

**A Constituição brasileira em uma linguagem que todo mundo entende.**

O **Constituição Simples** é um projeto open source, gratuito e de caráter educativo que busca aproximar a Constituição Federal de 1988 da realidade das pessoas. A proposta é facilitar a consulta a direitos, deveres e princípios constitucionais por meio do **texto oficial preservado**, de explicações em linguagem simples, de exemplos do cotidiano e de um glossário jurídico.

A plataforma será desenvolvida com foco em **acessibilidade, navegação por temas e experiência Mobile First**. O objetivo é ampliar o acesso à informação constitucional e incentivar a compreensão dos direitos fundamentais, sem substituir o texto legal ou a orientação de profissionais do Direito.

> **Escopo do MVP:** a primeira versão não pretende disponibilizar toda a Constituição. O lançamento será progressivo, começando por uma seleção de artigos e dispositivos relevantes para a vida cotidiana, incluindo direitos e garantias fundamentais, direitos sociais, democracia, igualdade e combate à discriminação, além de direitos dos povos indígenas. O texto constitucional original de cada dispositivo publicado permanecerá acessível.

## Tecnologias

### Backend e persistência — implementados

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

- **Python 3.12+** e **FastAPI** para o backend (estrutura e persistência em desenvolvimento; endpoints públicos ainda não implementados).
- **SQLAlchemy 2** para modelagem e acesso ao banco.
- **PostgreSQL 17** para persistência relacional.
- **Alembic** para migrações de esquema.
- **Docker Compose** para execução local do PostgreSQL.
- **Pytest** para testes de modelagem e integração.
- **Pydantic Settings** para configuração por variáveis de ambiente.

### Frontend — planejado

![React](https://img.shields.io/badge/React-149ECA?style=for-the-badge&logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

A interface web está planejada com **React, TypeScript e Tailwind CSS**, priorizando dispositivos móveis, leitura confortável e navegação acessível. A implementação do frontend ainda não começou.

### IA para preparação de conteúdo — integração inicial testada

![OpenRouter](https://img.shields.io/badge/OpenRouter-412991?style=for-the-badge&logo=openai&logoColor=white)

O **OpenRouter** foi testado como possível meio de acesso a modelos de linguagem. O pipeline definitivo de geração, validação e publicação de conteúdo ainda será implementado.

Outras ferramentas previstas ou utilizadas no desenvolvimento incluem **Git, HTTPX e Ruff**.

## Funcionalidades do MVP

- **Seleção temática de dispositivos constitucionais:** publicação gradual de artigos, parágrafos e incisos prioritários.
- **Texto constitucional original:** exibição separada e identificada, preservando a redação da fonte oficial.
- **Explicações em linguagem simples:** textos educativos para facilitar a compreensão de dispositivos selecionados.
- **Exemplos cotidianos:** situações práticas relacionadas aos direitos e deveres apresentados.
- **Glossário jurídico:** definições acessíveis de termos recorrentes.
- **Navegação por temas:** acesso a conteúdos por assunto, além do número do artigo.
- **Busca:** localização de artigos e conteúdos publicados.
- **Leitura comparada:** apresentação clara do texto original e da explicação correspondente.
- **Mobile First e acessibilidade:** interface responsiva, com atenção à legibilidade e à navegação.

**Fora do MVP:** chatbot jurídico, RAG, geração de explicações em tempo real, autenticação de usuários e cobertura integral imediata da Constituição.

## Como será utilizada a inteligência artificial?

A IA será utilizada **nos bastidores, antes da publicação**, e não durante a navegação dos visitantes. O fluxo planejado é:

1. Consultar a redação vigente da Constituição Federal em fonte oficial, prioritariamente o [Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm).
2. Selecionar e estruturar artigos e dispositivos prioritários, registrando referências e informações da fonte.
3. Gerar previamente explicações simplificadas, exemplos cotidianos e definições de glossário com auxílio de modelos de linguagem.
4. Aplicar verificações automáticas, critérios de risco e revisão humana dentro da capacidade disponível.
5. Armazenar os conteúdos e seus metadados no PostgreSQL, com controle de revisão e publicação.
6. Disponibilizar apenas o conteúdo selecionado para publicação, sem chamadas ao modelo de IA a cada acesso.

O **texto oficial não será reescrito pela IA**. Explicações e exemplos serão identificados como material educativo complementar.

> **Aviso:** verificações automáticas e revisão humana limitada não equivalem a uma revisão jurídica profissional integral. O projeto não oferece consultoria jurídica nem substitui a consulta à legislação vigente e a profissionais habilitados. O processo de publicação deve considerar a sensibilidade e o risco de cada conteúdo.

## Estrutura do projeto

A organização abaixo representa os principais diretórios e arquivos conhecidos nesta fase. Novos módulos serão adicionados conforme os próximos épicos.

```text
Constitui-o-Simples/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── article.py
│   │       ├── article_theme.py
│   │       ├── theme.py
│   │       ├── article_explanation.py
│   │       ├── practical_example.py
│   │       └── glossary_term.py
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── 14e6b15612f4_*.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_models.py
│   │   └── test_database.py
│   ├── scripts/
│   │   └── test_openrouter.py
│   ├── alembic.ini
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   ├── .env.example
│   ├── .env          # local; não versionar
│   └── .env.test     # local; não versionar
├── frontend/         # planejado
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

## Modelagem do banco de dados

O esquema inicial possui **seis tabelas da aplicação**:

| Tabela | Responsabilidade |
| --- | --- |
| `articles` | Identificação, texto original, estrutura opcional e rastreabilidade da fonte dos artigos. |
| `themes` | Temas utilizados na organização dos conteúdos. |
| `article_themes` | Relacionamento muitos-para-muitos entre artigos e temas. |
| `article_explanations` | Explicações simplificadas, referência ao dispositivo, modelo de IA e estado de revisão/publicação. |
| `practical_examples` | Exemplos cotidianos associados a artigos. |
| `glossary_terms` | Termos jurídicos e definições acessíveis. |

O Alembic mantém adicionalmente a tabela técnica `alembic_version`.

A migração inicial é **`14e6b15612f4`**. O esquema foi aplicado e conferido nos bancos de desenvolvimento e de testes. O comando `alembic check` não detectou operações pendentes na última verificação informada.

## Ambiente local

### Pré-requisitos

- Python 3.12 ou superior;
- Docker com Docker Compose;
- dependências Python indicadas nos arquivos `requirements.txt` e `requirements-dev.txt`.

### 1. Criar e ativar o ambiente virtual

Na raiz do repositório:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar as dependências

```bash
cd backend
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

### 3. Configurar o ambiente

Configure as variáveis do PostgreSQL no `.env` utilizado pelo Docker Compose e a URL de conexão no arquivo `backend/.env`, conforme os respectivos arquivos de exemplo disponíveis no projeto.

Exemplo de formato da URL do backend (substitua pelos valores locais):

```dotenv
DATABASE_URL=postgresql+psycopg://USUARIO:SENHA@127.0.0.1:5432/constituicao_simples
```

**Nunca versione arquivos `.env` com credenciais.**

### 4. Iniciar o PostgreSQL

Na raiz do repositório:

```bash
docker compose up -d postgres
```

### 5. Aplicar as migrações

Dentro de `backend`, com o banco de desenvolvimento configurado:

```bash
python -m alembic upgrade head
python -m alembic current
```

A revisão esperada nesta etapa é `14e6b15612f4 (head)`.

## Testes

O projeto utiliza um banco separado para testes de integração:

| Banco | Uso |
| --- | --- |
| `constituicao_simples` | Desenvolvimento local. |
| `constituicao_simples_test` | Testes automatizados de integração. |

O arquivo local `backend/.env.test` deve conter uma `DATABASE_URL` apontando exclusivamente para `constituicao_simples_test`. O esquema desse banco também precisa receber as migrações antes dos testes.

Os testes de integração utilizam transações com rollback para não manter registros fictícios. **Não execute testes de integração contra um banco com dados reais ou de produção.**

Dentro de `backend`:

```bash
# Testes de modelagem
python -m pytest tests/test_models.py -v

# Testes de integração
python -m pytest tests/test_database.py -v

# Suíte completa
python -m pytest tests/ -v

# Verificar diferenças entre modelos e esquema
python -m alembic check
```

**Validações confirmadas até aqui:** 25 testes de modelagem e os cinco primeiros testes de integração foram aprovados. A suíte consolidada de dez testes foi preparada, mas sua aprovação integral ainda precisa ser confirmada. A migração inicial e a verificação de consistência do Alembic foram executadas com sucesso.

## Roadmap

| Épico | Entrega | Situação |
| --- | --- | --- |
| **EP-01** | Backend, modelagem e persistência de dados | **Em finalização** — estrutura pronta; validação final da suíte e documentação. |
| **EP-02** | Curadoria e importação do texto constitucional | Planejado |
| **EP-03** | Geração antecipada de conteúdo com IA | Planejado |
| **EP-04** | Revisão, controle editorial e publicação | Planejado |
| **EP-05** | API pública de consulta | Planejado |
| **EP-06** | Frontend Mobile First | Planejado |
| **EP-07** | Testes, segurança, acessibilidade e qualidade | Planejado |
| **EP-08** | Deploy e lançamento do MVP | Planejado |

### EP-01 — Critérios de conclusão

- [x] Preparar ambiente Python e dependências.
- [x] Configurar PostgreSQL 17 no Docker Compose.
- [x] Configurar SQLAlchemy e Alembic.
- [x] Implementar os modelos e relacionamentos iniciais.
- [x] Aplicar a migração inicial nos bancos de desenvolvimento e testes.
- [x] Validar conexão e persistência de artigos, temas, explicações e exemplos.
- [x] Validar exclusão em cascata no PostgreSQL.
- [x] Confirmar `alembic check` sem alterações pendentes.
- [x] Confirmar aprovação da suíte consolidada de testes de integração e modelagem.
- [x] Revisar documentação, arquivos ignorados pelo Git e registrar o commit de conclusão.

## Princípios do projeto

- **Fidelidade à fonte:** o texto constitucional original é preservado e identificado.
- **Clareza:** explicações acessíveis sem ocultar nuances jurídicas importantes.
- **Transparência:** distinção explícita entre lei, explicação educativa e conteúdo gerado com apoio de IA.
- **Acesso público:** consulta gratuita, sem necessidade de conta no MVP.
- **Evolução gradual:** priorização de dispositivos relevantes, com expansão progressiva.
- **Privacidade e segurança:** credenciais fora do repositório e separação de ambientes.

## Licença

A licença open source ainda será definida antes da primeira versão pública. Até a inclusão de um arquivo `LICENSE`, não há uma licença de reutilização de código expressamente concedida pelo repositório.

---

**Constituição Simples — Conhecer seus direitos não deveria ser complicado.**
