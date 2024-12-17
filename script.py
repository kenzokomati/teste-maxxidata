import os
import requests
import pandas as pd
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Handler da API
def fetch_data(api_url):
    data = []
    
    try:
        # Faz a request para pegar dados da URL(api_url)
        response = requests.get(f"{api_url}", timeout=10)
        # Faz um raise para verificar em caso de erro na request
        response.raise_for_status() 
        # Extracao de dados tipo json para lista 'data'
        data.extend(response.json().get('results', []))
    # Handling de erro do raise/try
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {api_url}: {e}")
    
    return data

# Modularizacao para aplicar transformacao em todos elementos 
def clean_data(df):
    
    def clean_elements(value):
        # Se o elemento existir no campo
        if isinstance(value, str):
            # Transformar texto em minusculo/caixa baixa(lowercase)
            value = value.lower()
            # Removendo com .sub todos caracteres sem ser letras de a-z sendo elas minusculas ou maisculas, numeros ou expressoes representando formatacao, i.e(\t, \n, espaco, ..)
            value = re.sub(r'[^a-zA-Z0-9\s]', '', value)
        return value
    
    # Aplicando a transformacao em todos elementos do daframe
    return df.applymap(clean_elements) 


# Salvar dados como csv
def save_csv(data, folder, filename):
    # Checando se o diretorio existe no sistema e criando caso nao exista 
    os.makedirs(folder, exist_ok=True)
    # Nomeando o diretorio com filename
    filepath = os.path.join(folder, filename)
    # Transformando dataframe em csv para salvar no diretorio(filepath)
    pd.DataFrame(data).to_csv(filepath, index=False)
    print(f"Arquivo salvo em: {filepath}")


def main():
    # URLs da API
    endpoints = {
        "people": "https://swapi.bry.com.br/api/people/",
        "planets": "https://swapi.bry.com.br/api/planets/",
        "films": "https://swapi.bry.com.br/api/films/"
    }
    
    # Loop para pegar todos endpoints
    for name, url in endpoints.items():
        # Pegando dados da API
        print(f"Iniciando ingestao de {name}...")
        raw_data = fetch_data(url)
        
        # Salvando dados na pasta raw
        save_csv(raw_data, "raw", f"{name}.csv")
        
        # Carregando em dataframe
        df = pd.DataFrame(raw_data)
        # Tratando/limpando dados do dataframe
        cleaned_df = clean_data(df)
        
        # Salvando dados tratados na pasta work
        save_csv(cleaned_df, "work", f"{name}_cleaned.csv")
        
    print("Processamento concluido.")


if __name__ == "__main__":
    main()
