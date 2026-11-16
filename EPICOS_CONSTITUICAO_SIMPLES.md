# Constituição Simples — Épicos e acompanhamento do MVP

**Atualizado em:** 15/11/2026  
**Objetivo:** plataforma web gratuita, *mobile first*, para apresentar dispositivos selecionados da Constituição Federal de 1988, preservando o texto oficial e oferecendo explicações acessíveis, exemplos cotidianos e glossário.

> **Convenção de status**
> - **DONE** — concluído e validado no escopo descrito.
> - **IN PROGRESS** — implementação em andamento.
> - **TODO** — planejado, ainda não iniciado ou sem evidência de execução.
> - **BLOCKED** — depende de pré-requisito não resolvido.
>
> Os épicos EP-02 em diante são uma **proposta de organização do roadmap**, não uma afirmação de que já foram formalmente aprovados. Atualize os status conforme commits, testes e entregas.

## Visão geral

| Épico | Nome | Status | Critério de conclusão |
|---|---|---|---|
| EP-01 | Fundação do backend, modelagem e persistência | **IN PROGRESS** | Modelos revisados, migração Alembic aplicada e testes de integração no PostgreSQL |
| EP-02 | Curadoria e importação da Constituição | **TODO** | Dispositivos prioritários selecionados, importados e vinculados à fonte oficial |
| EP-03 | Pipeline offline de conteúdo educativo com IA | **TODO** | Explicações, exemplos e glossário gerados em lote, rastreáveis e armazenados |
| EP-04 | Revisão, qualidade e publicação | **TODO** | Critérios de validação, estados e regras de publicação implementados |
| EP-05 | API pública de consulta | **TODO** | Endpoints de artigos, temas, busca, explicações e glossário testados |
| EP-06 | Frontend mobile first e acessibilidade | **TODO** | Interface responsiva com texto original, linguagem simples e navegação temática |
| EP-07 | Testes ponta a ponta, segurança e observabilidade | **TODO** | Fluxos essenciais validados, tratamento de erros, logs e verificações de segurança |
| EP-08 | Deploy, documentação e lançamento do MVP | **TODO** | Aplicação publicada, documentação operacional e checklist de lançamento concluídos |

## EP-01 — Fundação do backend, modelagem e persistência

**Status: IN PROGRESS**  
**Objetivo:** estabelecer modelos, relacionamentos, infraestrutura local e migrações reproduzíveis.

### Concluído

- [x] Estrutura inicial do backend em FastAPI e SQLAlchemy.
- [x] Modelos `Article`, `Theme`, `ArticleExplanation`, `PracticalExample` e `GlossaryTerm`.
- [x] Associação N:N `article_themes`.
- [x] Alembic inicializado e metadados SQLAlchemy configurados.
- [x] 14 testes de modelagem aprovados em execução anterior.
- [x] Ambiente Linux com Docker Compose.
- [x] PostgreSQL 17 em contêiner com volume persistente e healthcheck saudável.
- [x] Conexão SQLAlchemy → PostgreSQL validada.

### Em andamento / a confirmar

- [ ] Confirmar alteração de `ArticleExplanation.simplified_text` para `Text`, `nullable=False` e executar novamente os testes no Linux.
- [ ] Acrescentar `device_reference` às explicações para incisos/parágrafos.
- [ ] Definir rastreabilidade da fonte oficial: URL e data de conferência do texto constitucional.
- [ ] Definir metadados de revisão/publicação (`review_level`, `reviewed_at`, `published_at`) e estados válidos de `review_status`.
- [ ] Definir regra de publicação para exemplos e glossário, sem complexidade excessiva.
- [ ] Conferir migrações existentes em `alembic/versions` antes de gerar outra.
- [ ] Gerar/revisar migração inicial e aplicar em banco de desenvolvimento.
- [ ] Testar inserção, consulta, relacionamentos e exclusão em PostgreSQL real.
- [ ] Revisar `.gitignore` para excluir `.env` e segredos; manter `.env.example` sem credenciais.

**Critérios de aceite:** migração reproduzível em banco vazio; testes ORM e integração aprovados; nenhuma credencial versionada; modelos coerentes com o MVP.

## EP-02 — Curadoria e importação da Constituição

**Status: TODO**  
**Objetivo:** formar um catálogo inicial de dispositivos relevantes, sem importar toda a Constituição de uma vez.

- [ ] Definir seleção inicial de aproximadamente 25–35 artigos/dispositivos, sujeita à revisão do escopo.
- [ ] Priorizar direitos fundamentais, direitos sociais, racismo e discriminação, direitos indígenas, democracia e situações cotidianas.
- [ ] Utilizar a versão vigente publicada pelo Planalto como referência principal.
- [ ] Preservar a redação original e a estrutura de caput, parágrafos, incisos e alíneas.
- [ ] Associar artigos a temas; evitar duplicações.
- [ ] Registrar origem e data de conferência dos textos.
- [ ] Criar rotina de importação idempotente e testes de integridade.

**Critérios de aceite:** conjunto inicial consultável no banco, fiel à fonte e organizado por temas.

## EP-03 — Pipeline offline de conteúdo educativo com IA

**Status: TODO**  
**Objetivo:** produzir antecipadamente explicações, exemplos e termos, sem custo de inferência a cada acesso do cidadão.

- [ ] Definir prompts e formato estruturado de saída.
- [ ] Implementar geração em lote, fora do fluxo de requisições da API.
- [ ] Registrar modelo de IA, data e dispositivo de origem.
- [ ] Gerar explicações claras sem substituir nem alterar o texto constitucional original.
- [ ] Gerar exemplos cotidianos e definições de glossário.
- [ ] Validar formato, campos obrigatórios, referências e duplicações antes de salvar.
- [ ] Garantir que conteúdos recém-gerados não sejam publicados automaticamente.

**Critérios de aceite:** lote reproduzível, resultados persistidos com rastreabilidade e publicação bloqueada por padrão.

## EP-04 — Revisão, qualidade e publicação

**Status: TODO**  
**Objetivo:** reduzir risco de explicações incorretas ou desatualizadas, respeitando a capacidade limitada de revisão humana.

- [ ] Formalizar estados: pendente, aprovado, rejeitado e publicado (ou fluxo equivalente).
- [ ] Definir níveis de verificação e critérios de prioridade por risco.
- [ ] Criar verificações automáticas de consistência com o dispositivo original.
- [ ] Definir quando exigir revisão humana e quando impedir publicação.
- [ ] Registrar datas e tipo de revisão; não declarar revisão jurídica inexistente.
- [ ] Exibir aviso educativo e referência à fonte oficial.
- [ ] Definir processo para corrigir ou retirar conteúdo após alterações constitucionais.

**Critérios de aceite:** apenas conteúdo elegível é exposto publicamente; origem e nível de validação são transparentes.

## EP-05 — API pública de consulta

**Status: TODO**  
**Objetivo:** fornecer dados ao frontend com endpoints simples, previsíveis e testados.

- [ ] Listar artigos e consultar artigo por identificador/número.
- [ ] Listar temas e artigos por tema.
- [ ] Expor texto original e conteúdo educativo publicado.
- [ ] Consultar glossário.
- [ ] Implementar busca básica e paginação quando necessário.
- [ ] Definir schemas Pydantic, tratamento de erros e testes de API.
- [ ] Impedir exposição de rascunhos e conteúdos rejeitados.

**Critérios de aceite:** endpoints documentados e testados, com filtragem de publicação.

## EP-06 — Frontend mobile first e acessibilidade

**Status: TODO**  
**Objetivo:** oferecer leitura fácil e navegação acessível, especialmente no celular.

- [ ] Definir identidade visual simples e responsiva.
- [ ] Criar página inicial com temas e busca.
- [ ] Exibir artigo original ao lado ou em alternância com explicação simples.
- [ ] Apresentar exemplos cotidianos e termos do glossário em contexto.
- [ ] Implementar estados de carregamento, vazio e erro.
- [ ] Garantir navegação por teclado, contraste, hierarquia semântica e legibilidade.
- [ ] Testar em diferentes larguras de tela.

**Critérios de aceite:** principais jornadas funcionais em celular e desktop, sem exigir login.

## EP-07 — Testes ponta a ponta, segurança e observabilidade

**Status: TODO**  
**Objetivo:** verificar o produto integrado e preparar operação confiável.

- [ ] Testes E2E de busca, navegação temática e leitura de artigos.
- [ ] Testes de acessibilidade e usabilidade com pessoas usuárias.
- [ ] Verificação de segredos, dependências e configurações de produção.
- [ ] Logs e tratamento de falhas sem expor dados sensíveis.
- [ ] Verificar comportamento de conteúdo não publicado.
- [ ] Definir rotina de backup e recuperação do PostgreSQL.

**Critérios de aceite:** fluxos críticos aprovados e problemas prioritários corrigidos.

## EP-08 — Deploy, documentação e lançamento do MVP

**Status: TODO**  
**Objetivo:** publicar uma primeira versão educativa e sustentável.

- [ ] Definir hospedagem e configuração de produção.
- [ ] Preparar deploy de API, frontend e banco com variáveis seguras.
- [ ] Executar migrações de produção com procedimento de rollback/backup.
- [ ] Publicar documentação de uso, limitações e fontes oficiais.
- [ ] Configurar monitoramento básico e rotina de manutenção.
- [ ] Validar checklist de lançamento e publicar MVP.

**Critérios de aceite:** site público, funcional, documentado e com processo básico de atualização.

## Fora do escopo do MVP 1.0

- Chatbot ou RAG para perguntas em tempo real.
- Geração de explicações sob demanda para visitantes.
- Cadastro/login de usuários.
- Cobertura integral de todos os dispositivos da Constituição no lançamento.
- Sistema editorial complexo ou promessa de revisão jurídica integral.

## Próxima ação recomendada

**EP-01 — tarefa imediata:** confirmar a correção de `simplified_text`, rodar os testes no Linux e, em seguida, implementar os metadados mínimos de rastreabilidade/revisão antes da primeira migração Alembic.

**Comandos de validação (dentro de `backend/`):**

```bash
python -m pytest tests/test_models.py -v
python -c "from app.models.article_explanation import ArticleExplanation; c = ArticleExplanation.__table__.columns['simplified_text']; print(c.type, c.nullable)"
```

**Resultado esperado para o campo:** `TEXT False`.
