def obter_fator_climatico(condicao_climatica):
    """
    Calcula o Fator Climático (FC) com base na condição climática.

    Args:
        condicao_climatica (str): A condição climática atual.
                                  Valores aceitos: "tempo bom", "chuva leve",
                                  "chuva moderada", "tempestade".

    Returns:
        float: O Fator Climático (FC) correspondente.
               Retorna 1.0 se a condição for desconhecida (assumindo tempo bom).
    """

    # Dicionário que mapeia as condições climáticas aos seus respectivos FCs
    # Podemos ajustar esses valores conforme a necessidade do projeto.
    fatores_climaticos = {
        "tempo bom": 1.0,
        "chuva leve": 1.2,
        "chuva moderada": 1.5,
        "tempestade": 2.0  # Um aumento significativo para tempestade
    }
    # --- LINHAS PARA DEBUG ---
    print(f"[DEBUG FC] Condição recebida: '{condicao_climatica}'")
    condicao_formatada = condicao_climatica.lower()
    print(f"[DEBUG FC] Condição formatada (lowercase): '{condicao_formatada}'")
    # --- FIM LINHAS PARA DEBUG ---

    # Verifica se a condição climática está no nosso dicionário
    # Se não estiver, assume FC = 1.0 (tempo bom) como padrão seguro
    fc = fatores_climaticos.get(condicao_formatada, 1.0)
    
    # --- LINHA PARA DEBUG ---
    print(f"[DEBUG FC] Fator Climático (FC) retornado: {fc}")
    # --- FIM LINHA PARA DEBUG ---
    # Verifica se a condição climática está no nosso dicionário
    # Se não estiver, assume FC = 1.0 (tempo bom) como padrão seguro
    fc = fatores_climaticos.get(condicao_climatica.lower(), 1.0)
    
    return fc

# --- Exemplos de Uso ---
if __name__ == "__main__":
    print("--- Testando o Fator Climático ---")

    # Exemplo 1: Tempo bom
    clima1 = "tempo bom"
    fc1 = obter_fator_climatico(clima1)
    print(f"Para '{clima1}', o Fator Climático (FC) é: {fc1}")

    # Exemplo 2: Chuva leve
    clima2 = "chuva leve"
    fc2 = obter_fator_climatico(clima2)
    print(f"Para '{clima2}', o Fator Climático (FC) é: {fc2}")

    # Exemplo 3: Chuva moderada
    clima3 = "chuva moderada"
    fc3 = obter_fator_climatico(clima3)
    print(f"Para '{clima3}', o Fator Climático (FC) é: {fc3}")

    # Exemplo 4: Tempestade
    clima4 = "tempestade"
    fc4 = obter_fator_climatico(clima4)
    print(f"Para '{clima4}', o Fator Climático (FC) é: {fc4}")

    # Exemplo 5: Condição desconhecida (deve retornar 1.0)
    clima5 = "neve" # Uma condição que não definimos
    fc5 = obter_fator_climatico(clima5)
    print(f"Para '{clima5}', o Fator Climático (FC) é: {fc5} (FC padrão)")