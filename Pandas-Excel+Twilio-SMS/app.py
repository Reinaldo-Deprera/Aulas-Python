import pandas as pd, os, locale
from twilio.rest import (
  Client,
  TwilioException
)
'''
Configurações / Variaveis de ambiente.
Lugares comuns para se colocar as variáveis:
  ../venv/bin/activate (exemplo)
  ~/.profile (linux)
  ... outros arquivos ...
  diretamente aqui, substituindo as instruções os.environ
  ou direto na memória
'''
twilio_account_sid  = os.environ['twilio_account_sid']
twilio_auth_token   = os.environ['twilio_auth_token']
twilio_phone_number = os.environ['twilio_phone_number']
celular_numero      = os.environ['celular_numero']

locale.setlocale(locale.LC_ALL, '')
meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in meses:
  tabela_vendas   = pd.read_excel(mes + '.xlsx')
  condicao        = tabela_vendas['Vendas'] > 55000
  if (condicao).any():
    valor_vendas = locale.currency(tabela_vendas.loc[condicao, 'Vendas'].values[0], grouping=True)
    mensagem = "No mês de {mes} o vendedor {nome} vendeu {valor}".format(
      mes=mes,
      nome=tabela_vendas.loc[condicao, 'Vendedor'].values[0],
      valor=valor_vendas
    )
    
    try:
      client = Client(twilio_account_sid, twilio_auth_token)
      envio = client.messages.create(
        body=mensagem,
        from_=twilio_phone_number,
        to=celular_numero
      )
      print("Torpedo SMS {id} enviado com sucesso!".format(id=envio.sid))
    except TwilioException as e:
      print(e)