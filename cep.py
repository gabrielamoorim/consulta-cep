import requests

cep = input('Digite o CEP:')

cep = cep.replace('-', '').replace('.', '').replace(' ', '')

if len(cep) == 8:
    
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao.json())
else:
    print('CEP INVÁLIDO')


