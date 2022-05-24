#importar as bibliotecas

import requests 
import json 

#resquisitar a API

requisicao =  requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL')

#desserializar o retorno da API 

cotacao = requisicao.json()

#escolhendo a moeda 

print('1 - Dólar; 2 - Euro; 3 - Bitcoin\n')

moeda = int(input(print('Qual moeda cotar hoje? \n ')))


#manipulando os dados

if (moeda==1):

	print(f'------Cotação Dólar------\n')
	print(f'Moeda: ' + cotacao['USD']['name'])
	print(f'Data: ' + cotacao['USD']['create_date'])
	print(f'Valor: ' + cotacao['USD']['bid'] + '\n')

elif (moeda==2):
	print(f'------Cotação Euro------\n')
	print(f'Moeda: ' + cotacao['EUR']['name'])
	print(f'Data: ' + cotacao['EUR']['create_date'])
	print(f'Valor: ' + cotacao['EUR']['bid'] + '\n')

elif (moeda==3): 
	print(f'------Cotação BTC------\n')
	print(f'Moeda: ' + cotacao['BTC']['name'])
	print(f'Data: ' + cotacao['BTC']['create_date'])
	print(f'Valor: ' + cotacao['BTC']['bid'] + '\n')

else:
	print('Moeda inválida')


