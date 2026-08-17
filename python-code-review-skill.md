---
name: python-code-review
description: Revisa código Python quanto a correção, formatação, legibilidade, manutenibilidade, tipagem, performance, segurança, testes e qualidade de implementação. Use ao revisar arquivos Python, pull requests, diffs, refatorações ou novas implementações.
---

# Revisão de Código Python

## Objetivo

Executar uma revisão criteriosa de código Python, priorizando problemas reais de engenharia em vez de preferências puramente estilísticas.

A revisão deve avaliar:

- correção;
- qualidade da implementação;
- legibilidade;
- manutenibilidade;
- convenções Python;
- formatação;
- tipagem;
- tratamento de erros;
- performance;
- segurança;
- testabilidade;
- complexidade desnecessária;
- duplicação de lógica;
- gerenciamento de recursos;
- uso de dependências.

O objetivo é identificar defeitos, riscos e melhorias relevantes sem propor reescritas desnecessárias.

---

## Princípios da revisão

### 1. Correção antes de estilo

Priorize os problemas nesta ordem:

1. bugs;
2. comportamento incorreto;
3. risco de perda ou corrupção de dados;
4. segurança;
5. concorrência e gerenciamento de recursos;
6. performance;
7. manutenibilidade;
8. tipagem;
9. formatação e estilo.

Não concentre a revisão em formatação enquanto existirem problemas funcionais mais relevantes.

---

### 2. Entenda o comportamento antes de sugerir mudanças

Antes de recomendar uma alteração:

1. entenda o objetivo do código;
2. inspecione o contexto ao redor quando disponível;
3. verifique chamadas e dependências relevantes;
4. inspecione testes existentes;
5. avalie se o comportamento é intencional.

Não classifique uma implementação como incorreta apenas porque existe outra forma mais elegante de escrevê-la.

---

### 3. Prefira mudanças pequenas e objetivas

Prefira mudanças focadas.

Não recomende:

- reescritas arquiteturais sem benefício concreto;
- novas abstrações para lógica usada apenas uma vez;
- design patterns sem necessidade;
- novas dependências para funcionalidades triviais;
- refatorações não relacionadas ao código revisado.

Sempre que sugerir uma refatoração, explique o benefício prático.

---

# Escopo da revisão

## 1. Correção

Procure problemas como:

- condicionais incorretas;
- expressões booleanas erradas;
- erros de limite;
- retornos ausentes;
- estados inconsistentes;
- pressupostos incorretos sobre entrada;
- mutação indevida de objetos;
- argumentos padrão mutáveis;
- comparação incorreta;
- uso incorreto de `is` e `==`;
- tratamento incorreto de `None`;
- estado compartilhado indevidamente;
- exceções mal tratadas;
- código inalcançável.

Exemplo problemático:

```python
def adicionar_item(item, itens=[]):
    itens.append(item)
    return itens
