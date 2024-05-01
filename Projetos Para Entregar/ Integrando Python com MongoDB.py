from pymongo import MongoClient

# Substitua 'your_connection_string' pela sua string de conexão
client = MongoClient('your_connection_string')
db = client['bank_database']  # Cria um novo banco de dados chamado 'bank_database'


# Definindo a coleção
customers = db['customers']

# Estrutura do documento para inserção
customer_data = {
    "nome": "João Silva",
    "cpf": "123456789",
    "endereco": "Rua ABC, 123",
    "contas": [
        {
            "tipo": "corrente",
            "agencia": "0001",
"num": 12345,
"saldo": 2000.50
},
{
"tipo": "poupança",
"agencia": "0001",
"num": 67890,
"saldo": 15000.75
}
]
}


### Passo 5: Executando Instruções de Recuperação de Informações

#Após inserir os dados, você pode realizar consultas para recuperar informações específicas usando pares de chave-valor, similar ao SQL, mas em um formato adequado para documentos NoSQL.

#**Exemplo 1: Recuperar todos os clientes**


for customer in customers.find():
    print(customer)
customer_by_cpf = customers.find_one({"cpf": "123456789"})
print(customer_by_cpf)
# Recuperar todas as contas do tipo 'corrente'
for customer in customers.find({"contas.tipo": "corrente"}):
    print(customer['nome'], customer['contas'])
for customer in customers.find({"contas.tipo": "corrente"}, {"nome": 1, "contas.$": 1}):
    print(customer)
