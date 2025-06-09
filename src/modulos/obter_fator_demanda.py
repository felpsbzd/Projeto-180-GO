def obter_fator_demanda(chamadas_por_minuto):
    """
    Calcula o Fator de Demanda (FD) com base no número de chamadas por minuto.

    Args:
        chamadas_por_minuto (float or int): O número de chamadas por minuto atual.

    Returns:
        float: O Fator de Demanda (FD) correspondente.
               Retorna 1.0 se o valor de chamadas for inválido (assume demanda normal).
    """

    if not isinstance(chamadas_por_minuto, (int, float)) or chamadas_por_minuto < 0:
        print(f"[ALERTA FD] Valor inválido para chamadas por minuto: {chamadas_por_minuto}. Assumindo FD = 1.0.")
        return 1.0

    # Classifica a demanda e retorna o FD correspondente
    if chamadas_por_minuto <= 5:
        # Baixa Demanda
        fd = 0.8
        nivel_demanda = "Baixa"
    elif 5 < chamadas_por_minuto <= 15:
        # Demanda Normal
        fd = 1.0
        nivel_demanda = "Normal"
    else:  # chamadas_por_minuto > 15
        # Alta Demanda
        fd = 1.3
        nivel_demanda = "Alta"

    print(f"[DEBUG FD] Chamadas por minuto: {chamadas_por_minuto} -> Nível de Demanda: {nivel_demanda} -> FD: {fd}")
    
    return fd

# --- Exemplos de Uso ---
if __name__ == "__main__":
    print("--- Testando o Fator de Demanda (FD) ---")

    # Exemplo 1: Baixa demanda
    cpm1 = 3
    fd1 = obter_fator_demanda(cpm1)
    print(f"Para {cpm1} chamadas/min, o Fator de Demanda (FD) é: {fd1}")

    # Exemplo 2: Limite superior da Baixa demanda
    cpm2 = 5
    fd2 = obter_fator_demanda(cpm2)
    print(f"Para {cpm2} chamadas/min, o Fator de Demanda (FD) é: {fd2}")

    # Exemplo 3: Limite inferior da Normal demanda
    cpm3 = 6
    fd3 = obter_fator_demanda(cpm3)
    print(f"Para {cpm3} chamadas/min, o Fator de Demanda (FD) é: {fd3}")

    # Exemplo 4: Limite superior da Normal demanda
    cpm4 = 15
    fd4 = obter_fator_demanda(cpm4)
    print(f"Para {cpm4} chamadas/min, o Fator de Demanda (FD) é: {fd4}")

    # Exemplo 5: Alta demanda
    cpm5 = 20
    fd5 = obter_fator_demanda(cpm5)
    print(f"Para {cpm5} chamadas/min, o Fator de Demanda (FD) é: {fd5}")

    # Exemplo 6: Valor inválido (negativo)
    cpm6 = -2
    fd6 = obter_fator_demanda(cpm6)
    print(f"Para {cpm6} chamadas/min, o Fator de Demanda (FD) é: {fd6} (FD padrão para inválidos)")

    # Exemplo 7: Valor inválido (não numérico)
    cpm7 = "abc"
    fd7 = obter_fator_demanda(cpm7)
    print(f"Para '{cpm7}' chamadas/min, o Fator de Demanda (FD) é: {fd7} (FD padrão para inválidos)")
