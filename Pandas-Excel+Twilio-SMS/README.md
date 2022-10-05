# **Processamento de Excel** e **envio de torpedo SMS** com **Pandas e Twilio**

- Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
- Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
- Caso não seja maior do que 55.000 não quero fazer nada

## Uso

1. Clonar repositório `git clone https://github.com/Reinaldo-Deprera/Aulas-Python`
2. Criar `Ambiente Virtual` para manter as dependências instaladas localmente `python -m venv venv`
2.1 (opcional) Se necessário, criar variáveis de ambiente no `Ambiente Virtual`, editando o arquivo `venv/bin/activate`
3. Carregar o Ambiente Virtual nos ambientes de execução e desenvolvimento da aplicação com o comando `source venv/bin/activate`
4. Instalar as dependências utilizadas na aplicação `pip install -r requirements.txt`

... ou seja:

```console
git clone https://github.com/Reinaldo-Deprera/Aulas-Python Aulas-Python &&
cd Aulas-Python/Pandas-Excel+Twilio-SMS &&
python -m venv venv &&
source venv/bin/activate &&
pip install -r requirements.txt
```

### Configuração

Configurar a aplicação editando os valores das variáveis abaixo, editando-as: diretamente no código; através de variáveis de ambiente; ou ainda, diretamente na memória:

```python
twilio_account_sid  = os.environ['twilio_account_sid']
twilio_auth_token   = os.environ['twilio_auth_token']
twilio_phone_number = os.environ['twilio_phone_number']
celular_numero      = os.environ['celular_numero']
```