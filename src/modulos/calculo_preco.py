# PROJETO-180-GO/src/modulos/calculo_preco.py

from src.modulos.obter_fator_climatico import obter_fator_climatico



def calcular_preco_final(preco_base, condicao_climatica):
    """
    Calcula o preço final de um produto/serviço aplicando o Fator Climático.

    Args:
        preco_base (float): O preço inicial do produto/serviço.
        condicao_climatica (str): A condição climática atual (ex: "tempo bom", "chuva leve").

    Returns:
        float: O preço final ajustado pelas condições climáticas.
    """
    if preco_base <= 0:
        raise ValueError("O preço base deve ser um valor positivo.")

    # 1. Obter o Fator Climático usando a função que já criamos
    fator_climatico = obter_fator_climatico(condicao_climatica)

    # 2. Calcular o preço final
    preco_final = preco_base * fator_climatico

    return preco_final

# --- Exemplos de Uso ---
if __name__ == "__main__":
    print("--- Testando o Cálculo do Preço Final ---")

    preco_inicial = 100.00 # Exemplo de preço base

    # Exemplo 1: Tempo bom
    clima1 = "tempo bom"
    preco_com_ajuste1 = calcular_preco_final(preco_inicial, clima1)
    print(f"Preço base: R${preco_inicial:.2f} | Condição: '{clima1}' | Preço Final: R${preco_com_ajuste1:.2f}")

    # Exemplo 2: Chuva leve
    clima2 = "chuva leve"
    preco_com_ajuste2 = calcular_preco_final(preco_inicial, clima2)
    print(f"Preço base: R${preco_inicial:.2f} | Condição: '{clima2}' | Preço Final: R${preco_com_ajuste2:.2f}")

    # Exemplo 3: Tempestade
    clima3 = "tempestade"
    preco_com_ajuste3 = calcular_preco_final(preco_inicial, clima3)
    print(f"Preço base: R${preco_inicial:.2f} | Condição: '{clima3}' | Preço Final: R${preco_com_ajuste3:.2f}")

    # Exemplo 4: Condição desconhecida (deve usar FC=1.0)
    clima4 = "vendaval"
    preco_com_ajuste4 = calcular_preco_final(preco_inicial, clima4)
    print(f"Preço base: R${preco_inicial:.2f} | Condição: '{clima4}' | Preço Final: R${preco_com_ajuste4:.2f}")

    # Exemplo 5: Teste com preço base inválido
    try:
        calcular_preco_final(-50.00, "tempo bom")
    except ValueError as e:
        print(f"Erro ao calcular preço com valor inválido: {e}")