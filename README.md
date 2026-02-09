# Process Classification by Scoring Rules (Python)

Python utility to validate numeric scores and automatically classify a process
based on configurable business rules and thresholds.

This project can be adapted for scenarios such as:
- process evaluation
- approval systems
- quality scoring
- rule-based decision automation

---

## Overview

The script receives a list of numeric scores, validates the input data and
classifies the process according to predefined rules.

The classification result can be:
- **Invalid Data**
- **Excellent**
- **Approved**
- **Rejected**

All rules and thresholds are fully configurable.

---

## Business Rules

- Scores must be non-negative values
- Scores greater than or equal to the minimum threshold are considered approved
- Final classification follows these rules:
  - **Invalid Data** → if any score is negative
  - **Excellent** → approved scores ≥ excellence threshold
  - **Approved** → approved scores ≥ minimum required
  - **Rejected** → does not meet minimum requirements

---

## Project Structure

- `validar_pontuacoes(pontuacoes)`
- `contar_aprovados(pontuacoes, minimo)`
- `classificar_processo(pontuacoes, minimo, quant_aprovados, quant_excelente)`

Each function has a single responsibility, making the code easy to maintain
and reuse in other systems.

---

## Example Usage

```python
pontuacoes = [7, 8, 9, 6, 10]

resultado = classificar_processo(
    pontuacoes,
    minimo=7,
    quant_aprovados=3,
    quant_excelente=5
)

print(resultado)
