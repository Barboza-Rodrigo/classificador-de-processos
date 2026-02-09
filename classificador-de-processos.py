def validar_pontuacoes(pontuacoes):
    """
    Verifica se todas as pontuações são válidas (não negativas).
    Retorna True se estiverem válidas, False caso contrário.
    """
    for item in pontuacoes:
        if item < 0:
            return False
    return True


def contar_aprovados(pontuacoes, minimo):
    """
    Conta quantas pontuações são maiores ou iguais ao valor mínimo.
    Retorna a quantidade de aprovados.
    """
    contador = 0
    for item in pontuacoes:
        if item >= minimo:
            contador += 1
    return contador


def classificar_processo(pontuacoes, minimo, quant_aprovados, quant_excelente):
    """
    Classifica o processo com base nas regras:
    - Dados inválidos: se houver pontuação negativa
    - Excelente: se aprovados >= quant_excelente
    - Aprovado: se aprovados >= quant_aprovados
    - Reprovado: caso contrário
    """
    if not validar_pontuacoes(pontuacoes):
        return "Dados inválidos"

    aprovados = contar_aprovados(pontuacoes, minimo)

    if aprovados >= quant_excelente:
        return "Excelente"
    elif aprovados >= quant_aprovados:
        return "Aprovado"
    else:
        return "Reprovado"
