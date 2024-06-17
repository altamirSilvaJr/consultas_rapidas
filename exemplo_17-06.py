import requests
import base64
import boto3
from io import BytesIO
from datetime import datetime, timedelta

def api_call(api_url, bucket, path):
    response = requests.get(f'api_url?bucket={bucket}&key={path}') 
    if response.status_code == 200:
        return response.json().get('response') # MUDAR AQUI
    else:
        return "FAILED"

def save_parquet(base64_data, bucket_name, file_name):
    decoded_data = base64.b64decode(base64_data)
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=decoded_data)

api_url = ''
bucket_origem = ''
bucket_destino = ''

lista_tabelas = ['t1', 't2'] # adicionar tabelas na lista

for tabela in lista_tabelas:
    data_final = datetime.now() # mudar
    data_inicial = datetime.now() - timedelta(days=5) # mudar
    while data_inicial < data_final:
        path = f'{tabela}/partition_year={data_inicial.year}/partition_month={data_inicial.month}/partition_day={data_inicial.day}/'
        data = api_call(api_url, bucket_origem, path)
        save_parquet(data, bucket_destino, f'{tabela}.parquet')
        ##### ADICIONAR AQUI A CLASSE PARTITION_MANAGER PARA CRIAR AS PARTIÇÕES
        data_inicial = data_inicial + timedelta(days=1)
