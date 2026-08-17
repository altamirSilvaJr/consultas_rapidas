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
```

Prefira:

```python
def adicionar_item(
    item: str,
    itens: list[str] | None = None,
) -> list[str]:
    if itens is None:
        itens = []

    itens.append(item)
    return itens
```

---

## 2. Python idiomático

Identifique construções desnecessariamente verbosas ou pouco idiomáticas.

Prefira:

```python
if valor is None:
```

em vez de:

```python
if valor == None:
```

Prefira:

```python
if itens:
```

em vez de:

```python
if len(itens) > 0:
```

quando a intenção for apenas verificar se a coleção possui elementos.

Prefira:

```python
for item in itens:
```

em vez de manipular índices manualmente quando o índice não for necessário.

Não sugira construções mais "pythônicas" se elas reduzirem a clareza.

---

## 3. Formatação e estilo

Avalie o código de acordo com as convenções modernas de Python e com as ferramentas configuradas no projeto.

Verifique:

- indentação;
- comprimento de linha;
- linhas em branco;
- ordem de imports;
- imports não utilizados;
- espaços;
- nomes;
- tamanho de funções;
- organização de classes;
- comentários desnecessários;
- expressões excessivamente complexas.

Quando disponíveis, respeite as configurações existentes em:

```text
pyproject.toml
ruff.toml
setup.cfg
tox.ini
```

Não imponha regras conflitantes com o próprio repositório.

---

## 4. Nomenclatura

Verifique se os nomes representam claramente sua responsabilidade.

Avalie:

- variáveis;
- funções;
- métodos;
- classes;
- módulos;
- constantes;
- exceções.

Evite nomes genéricos quando houver alternativa mais específica.

Evite:

```python
data
value
obj
temp
manager
helper
process
do_stuff
```

Prefira nomes relacionados ao domínio, como:

```python
telemetry_packet
calculate_fuel_consumption()
TelemetryPacketParser
```

Não torne nomes desnecessariamente longos.

---

## 5. Design de funções

Verifique:

- excesso de responsabilidades;
- muitos argumentos;
- efeitos colaterais ocultos;
- condicionais muito profundas;
- lógica duplicada;
- retornos pouco claros;
- níveis diferentes de abstração dentro da mesma função.

Extraia funções quando isso:

- melhora reutilização;
- melhora testabilidade;
- reduz duplicação;
- melhora significativamente a leitura.

Não extraia funções apenas para diminuir o número de linhas.

---

## 6. Classes e orientação a objetos

Verifique:

- responsabilidades excessivas;
- herança desnecessária;
- estado mutável escondido;
- acoplamento elevado;
- métodos estáticos desnecessários;
- classes sem necessidade;
- excesso de getters e setters;
- construtores executando operações pesadas.

Prefira composição quando ela reduzir acoplamento.

Evite criar classes quando uma função ou módulo simples for suficiente.

Tenha atenção especial a classes genéricas como:

```text
Manager
Utils
Helper
Processor
Service
```

quando acumularem responsabilidades não relacionadas.

---

## 7. Type hints

Verifique se interfaces públicas e funções relevantes possuem anotações úteis.

Prefira:

```python
def get_user(user_id: str) -> User | None:
    ...
```

Evite tipos excessivamente genéricos como:

```python
Any
dict
list
object
```

quando tipos mais precisos forem viáveis.

Considere:

```python
dict[str, int]
list[str]
Sequence[str]
Mapping[str, str]
Protocol
TypedDict
dataclass
```

quando apropriado.

Não introduza tipagem excessivamente complexa sem benefício real.

---

## 8. Estruturas de dados

Avalie se a estrutura de dados utilizada é adequada.

Considere:

- `set` para verificações frequentes de pertencimento;
- `dict` para buscas por chave;
- `deque` para comportamento de fila;
- `dataclass` para dados estruturados;
- `Enum` para conjuntos finitos de estados;
- generators para processamento incremental.

Exemplo:

```python
if user_id in user_ids:
```

Se `user_ids` for grande e pesquisado repetidamente, avalie se deveria ser um `set`.

Só sinalize quando houver impacto prático.

---

## 9. Tratamento de erros

Procure padrões problemáticos como:

```python
try:
    operation()
except Exception:
    pass
```

Verifique:

- exceções ignoradas;
- `except` excessivamente amplo;
- mensagens pouco informativas;
- exceções usadas como fluxo normal;
- perda do traceback original;
- falta de cleanup;
- retries inadequados.

Prefira:

```python
try:
    operation()
except ConnectionError as exc:
    raise TelemetryConnectionError(
        "Não foi possível conectar à fonte de telemetria."
    ) from exc
```

Não capture exceções que não possam ser tratadas de forma adequada naquela camada.

---

## 10. Gerenciamento de recursos

Verifique se recursos são liberados corretamente.

Avalie:

- arquivos;
- sockets;
- conexões de banco;
- clientes HTTP;
- arquivos temporários;
- subprocessos;
- locks.

Prefira context managers quando possível.

Exemplo:

```python
with open(path, encoding="utf-8") as file:
    content = file.read()
```

---

## 11. Performance

Procure problemas relevantes de performance, como:

- loops aninhados desnecessários;
- repetição de operações custosas;
- múltiplas queries redundantes;
- chamadas repetidas à mesma API;
- leitura integral de arquivos grandes sem necessidade;
- serialização repetida;
- cópias desnecessárias;
- recriação frequente de clientes;
- buscas ineficientes em coleções;
- ordenação sem necessidade;
- padrão N+1.

Não sugira micro-otimizações sem impacto prático.

Priorize:

1. problemas algorítmicos;
2. I/O;
3. uso de memória;
4. micro-otimizações.

---

## 12. Iterações e coleções

Evite criação desnecessária de coleções intermediárias.

Exemplo:

```python
values = [transform(item) for item in items]

for value in values:
    consume(value)
```

Considere:

```python
for item in items:
    consume(transform(item))
```

ou:

```python
values = (transform(item) for item in items)
```

Use generators apenas quando a avaliação lazy realmente trouxer benefício.

---

## 13. Comprehensions

Prefira comprehensions quando continuarem legíveis.

Bom:

```python
active_users = [
    user
    for user in users
    if user.is_active
]
```

Evite comprehensions excessivamente aninhadas.

Quando a lógica for complexa, prefira um loop explícito.

Legibilidade tem prioridade sobre redução do número de linhas.

---

## 14. Segurança

Procure problemas como:

- credenciais hardcoded;
- API keys;
- senhas;
- tokens;
- desserialização insegura;
- SQL injection;
- command injection;
- `subprocess` inseguro;
- path traversal;
- arquivos temporários inseguros;
- aleatoriedade inadequada;
- dados sensíveis em logs.

Sinalize padrões como:

```python
subprocess.run(
    command,
    shell=True,
)
```

quando entrada não confiável puder chegar ao comando.

Sinalize SQL construído via interpolação:

```python
query = f"SELECT * FROM users WHERE id = {user_id}"
```

Prefira queries parametrizadas.

Nunca exponha valores reais de segredos durante a revisão.

---

## 15. Logging

Verifique:

- uso de `print()` como logging;
- dados sensíveis em logs;
- logs excessivos dentro de loops;
- nível de log inadequado;
- ausência de contexto;
- exceções registradas duplicadamente.

Prefira logging estruturado quando o projeto já possuir suporte.

Nunca sugira registrar:

- senhas;
- tokens;
- API keys;
- credenciais;
- payloads sensíveis.

---

## 16. Chamadas externas

Ao revisar integrações com:

- APIs HTTP;
- AWS;
- bancos de dados;
- filas;
- sistemas de arquivos;
- subprocessos;

verifique:

- timeout;
- retry;
- erros transitórios;
- reaproveitamento de conexão;
- rate limit;
- falhas parciais.

Chamadas de rede devem preferencialmente possuir timeout explícito.

Não adicione retries indiscriminadamente.

---

## 17. Concorrência e código assíncrono

Verifique:

- estado mutável compartilhado;
- race conditions;
- locks;
- operações bloqueantes em funções `async`;
- segurança entre threads;
- cancelamento de tasks;
- tasks abandonadas;
- propagação de exceções.

Exemplo problemático:

```python
async def handler():
    time.sleep(5)
```

Prefira:

```python
async def handler():
    await asyncio.sleep(5)
```

quando aplicável.

---

## 18. Testes

Avalie se a implementação possui cobertura adequada.

Procure:

- comportamento novo sem teste;
- ausência de edge cases;
- testes sem assertions significativas;
- testes acoplados à implementação;
- excesso de mocks;
- testes não determinísticos;
- setup duplicado.

Caminhos relevantes normalmente devem contemplar:

- happy path;
- entradas inválidas;
- casos de borda;
- cenários de falha.

Não exija testes para código trivial sem benefício real.

---

## 19. Qualidade dos testes

Avalie testes com o mesmo rigor aplicado ao código de produção.

Prefira uma estrutura clara de:

```text
arrange
act
assert
```

ou:

```text
given
when
then
```

Evite testes que apenas verifiquem que o código não lançou exceção quando há um resultado concreto que pode ser validado.

---

## 20. Dependências

Ao identificar novas dependências, verifique:

- se são realmente necessárias;
- se outra dependência já cobre a necessidade;
- se a biblioteca padrão é suficiente;
- se a dependência aumenta significativamente a complexidade.

Evite dependências novas para funcionalidades triviais.

---

## 21. Código duplicado

Identifique duplicações relevantes.

Não recomende abstração automaticamente após duas ocorrências semelhantes.

Sugira extração quando a duplicação causar:

- risco de manutenção;
- comportamento inconsistente;
- correções duplicadas;
- repetição significativa de lógica.

Uma pequena duplicação pode ser melhor que uma abstração prematura.

---

## 22. Comentários e documentação

Comentários devem explicar:

- por que algo existe;
- restrições importantes;
- comportamento não óbvio;
- limitações externas.

Evite comentários que apenas repetem o código.

Ruim:

```python
# Incrementa contador
counter += 1
```

Melhor:

```python
# O identificador do pacote reinicia após uma reconexão,
# portanto não pode ser tratado como identificador global.
packet_id += 1
```

Verifique docstrings de interfaces públicas quando o projeto exigir.

---

## 23. Código morto

Procure:

- funções sem uso;
- branches inalcançáveis;
- variáveis não utilizadas;
- código legado sem necessidade;
- blocos comentados;
- feature flags abandonadas.

Não recomende remoção de código sem verificar usos.

Pesquise referências antes de classificar APIs públicas como código morto.

---

## 24. Melhorias de implementação

Avalie se o comportamento atual pode ser implementado de forma mais simples ou segura.

Considere:

- complexidade desnecessária;
- estado desnecessário;
- abstrações excessivas;
- transformações repetidas;
- múltiplas passagens pelos mesmos dados;
- acoplamento elevado;
- responsabilidades mal separadas;
- dependências mal definidas.

Para cada melhoria proposta, explique o benefício concreto.

Boas justificativas incluem:

- elimina bug;
- reduz duplicação;
- melhora testabilidade;
- reduz complexidade;
- evita I/O desnecessário;
- melhora tratamento de falhas;
- facilita manutenção.

"Fica mais limpo" não é justificativa suficiente para uma refatoração grande.

---

## 25. Compatibilidade

Antes de sugerir mudanças em comportamento público, verifique impacto em:

- assinaturas de funções;
- construtores;
- tipos retornados;
- exceções;
- configuração;
- formatos serializados;
- variáveis de ambiente;
- schemas;
- contratos de API.

Riscos de quebra de compatibilidade devem ser explicitamente sinalizados.

---

# Severidade dos achados

## CRÍTICO

Problemas que podem causar:

- perda de dados;
- vulnerabilidade grave;
- falha catastrófica em produção;
- corrupção irreversível.

Exemplo:

```text
[CRÍTICO] Entrada fornecida pelo usuário é enviada diretamente ao shell,
permitindo execução arbitrária de comandos.
```

---

## ALTO

Problemas com alta probabilidade de causar comportamento incorreto ou falhas importantes.

Exemplos:

- bug de lógica;
- race condition;
- transação incorreta;
- erro grave de tratamento de exceção;
- vazamento relevante de recursos.

---

## MÉDIO

Problemas com impacto relevante em:

- manutenibilidade;
- confiabilidade;
- performance;
- testabilidade.

Exemplos:

- operações custosas repetidas;
- alto acoplamento;
- validação importante ausente;
- implementação frágil.

---

## BAIXO

Melhorias menores.

Exemplos:

- nomes pouco claros;
- complexidade pequena;
- tipagem;
- legibilidade.

---

## NIT

Observações estritamente opcionais ou estilísticas.

Use `NIT` com moderação.

Não permita que preferências estilísticas dominem a revisão.

---

# Formato de cada achado

Cada achado deve seguir este formato:

```text
[SEVERIDADE] Título curto

Local:
<arquivo>:<linha ou símbolo>

Problema:
Explique o que está errado.

Impacto:
Explique por que isso importa.

Recomendação:
Explique como melhorar.

Exemplo:
Inclua código somente quando realmente útil.
```

Exemplo:

```text
[ALTO] Argumento padrão mutável compartilha estado entre chamadas

Local:
src/cache.py:18 — Cache.add()

Problema:
A função utiliza uma lista como argumento padrão. Argumentos padrão são
avaliados apenas uma vez na definição da função, fazendo com que a mesma
lista seja reutilizada entre diferentes chamadas.

Impacto:
Valores de chamadas anteriores podem aparecer inesperadamente nas chamadas
seguintes.

Recomendação:
Use None como valor padrão e inicialize uma nova lista dentro da função.
```

---

# Evite falsos positivos

Não reporte algo apenas porque teoricamente poderia ser melhor.

Antes de criar um achado, verifique:

1. existe realmente um problema?
2. há risco ou impacto prático?
3. a recomendação melhora de fato o código?
4. o problema é relevante para a alteração revisada?
5. o repositório já utiliza esse padrão intencionalmente?

O objetivo da revisão é maximizar sinal e minimizar ruído.

---

# Revisão de diffs e pull requests

Ao revisar um diff ou pull request:

- concentre-se principalmente nos problemas introduzidos pela alteração;
- analise código existente somente quando necessário para entender o contexto;
- não transforme uma revisão pontual em uma auditoria completa do repositório.

Um problema antigo pode ser mencionado quando:

- a nova implementação o agrava;
- o código novo depende dele;
- ele representa risco direto para a mudança revisada.

---

# Ferramentas

Antes de sugerir mudanças de formatação, procure as configurações do projeto:

```text
pyproject.toml
ruff.toml
mypy.ini
pytest.ini
setup.cfg
tox.ini
```

Quando aplicável, execute:

```bash
ruff check .
ruff format --check .
mypy .
pytest
```

Em projetos Poetry:

```bash
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy .
poetry run pytest
```

Nunca afirme que um comando passou se ele não foi realmente executado.

---

# Ruff

Quando Ruff estiver configurado, respeite suas regras em vez de impor preferências pessoais.

Considere executar:

```bash
ruff check .
```

ou:

```bash
poetry run ruff check .
```

Por padrão, não aplique correções automaticamente durante uma revisão.

Quando o usuário pedir revisão e correção, as correções podem ser aplicadas.

---

# Formatação

Quando o código não seguir os padrões configurados, prefira recomendar o formatter do projeto.

Exemplos:

```bash
ruff format .
```

ou:

```bash
black .
```

Não reescreva grandes partes do código manualmente apenas para alterar formatação.

Problemas apenas de formatação devem normalmente ser classificados como `BAIXO` ou `NIT`.

---

# Type checking

Se `mypy` ou outro type checker estiver configurado, utilize-o quando adequado.

Diferencie:

- bugs de runtime;
- problemas de tipagem estática;
- ausência de annotations.

Não classifique um problema puramente de tipagem como bug de runtime sem evidência.

---

# Testes existentes

Sempre que possível:

1. localize os testes associados ao módulo alterado;
2. entenda o comportamento esperado;
3. identifique cenários não cobertos;
4. execute os testes relevantes.

Não altere testes apenas para esconder um bug na implementação.

Testes devem ser modificados quando o comportamento esperado mudar de forma intencional.

---

# Alteração automática de código

Por padrão, execute apenas a revisão.

Não modifique arquivos durante uma revisão, a menos que o usuário solicite explicitamente correções.

Quando o usuário pedir algo equivalente a:

```text
revise e corrija
```

execute:

1. revisão;
2. identificação dos problemas;
3. implementação das correções;
4. execução das validações relevantes;
5. revisão do diff final;
6. resumo das alterações.

Não corrija problemas não relacionados sem justificativa.

---

# Ao modificar código

Preserve o comportamento existente, exceto quando estiver corrigindo um problema identificado.

Prefira o menor patch coerente possível.

Não:

- faça refatorações não relacionadas;
- renomeie símbolos sem necessidade;
- reorganize módulos inteiros apenas por estilo;
- atualize dependências sem motivo;
- altere APIs públicas sem necessidade.

Após as alterações, sempre inspecione o diff final.

---

# Formato final da revisão

Comece pelos achados, ordenados por severidade.

Exemplo:

```text
## Achados

### ALTO

...

### MÉDIO

...

### BAIXO

...
```

Omita categorias que não possuam achados.

Depois apresente:

```text
## Validação

- pytest: passou / falhou / não executado
- ruff: passou / falhou / não executado
- mypy: passou / falhou / não executado
```

Finalize com:

```text
## Resumo

Resumo breve da qualidade geral da implementação e das principais melhorias.
```

---

# Quando nenhum problema for encontrado

Não invente problemas para tornar a revisão aparentemente mais completa.

Use algo como:

```text
## Achados

Nenhum problema relevante de correção, confiabilidade, segurança,
performance ou manutenibilidade foi identificado nas alterações revisadas.

## Validação

- pytest: passou
- ruff: passou
- mypy: não configurado

## Resumo

A implementação está consistente com os padrões existentes do projeto e
não requer alterações relevantes.
```

---

# Regra de prioridade

Durante a revisão, priorize:

```text
correção
    ↓
confiabilidade
    ↓
segurança
    ↓
manutenibilidade
    ↓
performance
    ↓
legibilidade
    ↓
formatação
```

Uma revisão que encontra problemas de formatação, mas deixa passar um bug funcional, é uma revisão inadequada.
