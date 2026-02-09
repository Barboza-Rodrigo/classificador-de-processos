# Classificador de Processos por Pontuação (Python)

Ferramenta em Python para validar pontuações numéricas e classificar processos
com base em regras de negócio configuráveis.

Este código pode ser adaptado para cenários como:
- avaliação de processos
- sistemas de aprovação
- classificação por critérios
- automação de decisões baseadas em regras

---

## Visão Geral

O script recebe uma lista de pontuações numéricas, valida os dados de entrada
e classifica o processo conforme regras definidas.

O resultado da classificação pode ser:
- **Dados inválidos**
- **Excelente**
- **Aprovado**
- **Reprovado**

Todas as regras e limites são configuráveis.

---

## Regras de Negócio

- Nenhuma pontuação pode ser negativa
- Pontuações maiores ou iguais ao valor mínimo são consideradas aprovadas
- A classificação final segue as regras:
  - **Dados inválidos** → se existir pontuação negativa
  - **Excelente** → quantidade de aprovados ≥ nível de excelência
  - **Aprovado** → quantidade de aprovados ≥ mínimo exigido
  - **Reprovado** → quando não atinge o mínimo

---

## Estrutura do Código

- `validar_pontuacoes(pontuacoes)`
- `contar_aprovados(pontuacoes, minimo)`
- `classificar_processo(pontuacoes, minimo, quant_aprovados, quant_excelente)`

Cada função possui uma responsabilidade clara, facilitando manutenção e
reutilização em outros sistemas.

---

## Exemplo de Uso

```python
pontuacoes = [7, 8, 9, 6, 10]

resultado = classificar_processo(
    pontuacoes,
    minimo=7,
    quant_aprovados=3,
    quant_excelente=5
)

print(resultado)
