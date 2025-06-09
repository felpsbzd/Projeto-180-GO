# Importa a função obter_fator_climatico
from src.modulos.obter_fator_climatico import obter_fator_climatico

# Importa a função obter_fator_demanda
from src.modulos.obter_fator_demanda import obter_fator_demanda

def calcular_preco_final(quilometros, tempo_minutos, condicao_climatica, chamadas_por_minuto):
    """
    Calcula o preço final de um produto/serviço aplicando:
    1. A fórmula de preço base: P(x,t) = 5 + 1.0x + 0.2t
    2. A SOMA do Fator Climático (FC) e do Fator de Demanda (FD), multiplicada pelo preço base.

    Args:
        quilometros (float): Distância em quilômetros (x na fórmula).
        tempo_minutos (float): Tempo em minutos (t na fórmula).
        condicao_climatica (str): Condição climática atual (ex: "tempo bom", "chuva leve").
        chamadas_por_minuto (float): Número de chamadas de demanda por minuto.

    Returns:
        float: O preço final ajustado por todos os fatores.
    """
    
    # 1. Validação dos parâmetros de entrada
    if not isinstance(quilometros, (int, float)) or quilometros < 0:
        print(f"[ALERTA PREÇO] Valor inválido para quilômetros: {quilometros}. Retornando 0.")
        return 0.0
    if not isinstance(tempo_minutos, (int, float)) or tempo_minutos < 0:
        print(f"[ALERTA PREÇO] Valor inválido para tempo em minutos: {tempo_minutos}. Retornando 0.")
        return 0.0

    # 2. Calcular o Preço Base usando a fórmula P(x,t) = 5 + 1.0x + 0.2t
    # Onde x = quilometros e t = tempo_minutos
    preco_base = 5 + (1.0 * quilometros) + (0.2 * tempo_minutos)
    
    # Adicionando uma validação simples para o preço base calculado
    if preco_base <= 0:
        print(f"[ALERTA PREÇO] Preço base calculado é zero ou negativo ({preco_base}). Retornando 0.")
        return 0.0

    # 3. Obter o Fator Climático (FC)
    fator_climatico = obter_fator_climatico(condicao_climatica)

    # 4. Obter o Fator de Demanda (FD)
    fator_demanda = obter_fator_demanda(chamadas_por_minuto)

    # 5. Calcular o Preço Final ajustado (AGORA COM SOMA DOS FATORES!)
    preco_final_ajustado = preco_base * (fator_climatico + fator_demanda)

    return preco_final_ajustado

# --- Exemplos de Uso ---
# --- Exemplos de Uso Interativo ---
if __name__ == "__main__":
    print("--- Calculadora de Preço Dinâmico ---")

    # Obter Quilômetros
    while True: # Loop para garantir entrada válida
        try:
            quilometros_str = input("Digite a distância em quilômetros (ex: 10.5): ")
            quilometros_input = float(quilometros_str)
            if quilometros_input < 0:
                print("Distância não pode ser negativa. Tente novamente.")
            else:
                break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para os quilômetros.")

    # Obter Tempo em Minutos
    while True:
        try:
            tempo_minutos_str = input("Digite o tempo em minutos (ex: 30): ")
            tempo_minutos_input = float(tempo_minutos_str)
            if tempo_minutos_input < 0:
                print("Tempo não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o tempo.")

    # Obter Condição Climática
    condicao_climatica_input = input("Digite a condição climática (tempo bom, chuva leve, chuva moderada, tempestade): ").lower()
    # Podemos adicionar validação aqui se necessário, mas por enquanto, a função obter_fator_climatico já trata desconhecidos

    # Obter Chamadas por Minuto
    while True:
        try:
            chamadas_por_minuto_str = input("Digite o número de chamadas por minuto (ex: 8): ")
            chamadas_por_minuto_input = float(chamadas_por_minuto_str)
            if chamadas_por_minuto_input < 0:
                print("Chamadas por minuto não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para as chamadas por minuto.")

    # Calcular e exibir o preço final
    preco_final_calculado = calcular_preco_final(
        quilometros=quilometros_input,
        tempo_minutos=tempo_minutos_input,
        condicao_climatica=condicao_climatica_input,
        chamadas_por_minuto=chamadas_por_minuto_input
    )

    print("\n--- Resultado do Cálculo ---")
    print(f"Distância: {quilometros_input:.2f} km")
    print(f"Tempo: {tempo_minutos_input:.2f} minutos")
    print(f"Condição Climática: {condicao_climatica_input}")
    print(f"Chamadas por Minuto: {chamadas_por_minuto_input:.2f}")
    print(f"Preço Final Ajustado: R${preco_final_calculado:.2f}")