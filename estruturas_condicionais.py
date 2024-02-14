'''
MAIOR_IDADE = 18

idade = int(input("informe sua idade"))

if idade >= MAIOR_IDADE:
    print("Mairo de idade, pode tirara habilitação")
    
if idade < MAIOR_IDADE:
    print("Ainda nao pode, tirar a Cnh")
    
if idade >= MAIOR_IDADE:
    print("Mairo de idade, pode tirara habilitação")
else:
    print("Ainda nao pode, tirar a Cnh")
'''
 # serve para comentar linha inteira enquanto 3 aspas ele comenta um escopo
 

'''
conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2000
cheque_especial = 450

if conta_normal: 
    if saldo >= saque :
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial): 
        print( "Saque realizado com uso cheque especial!")
    else:
        print("Saldo insuficiente !")

elif conta_universitaria:
    if saldo >= saque :
        print( "Saque realizado com sucesso!" )
    else:
        print( "Saldo insuficientel")

'''

'''
saldo = 2000
saque = 2000

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
'''    
'''
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)
        
        
pessoas_idades = {"Alice": 30, "Bob": 25, "Charlie": 35}
for nome, idade in pessoas_idades.items():
    print(f"{nome} tem {idade} anos")
'''

''' 
opcao = 1

while opcao != 0:
    opcao = int (input("informe um número:"))
    
    if opcao == 10:
        break
print(opcao)
'''

'''
opcao = True

while True:
    opcao = int (input("informe um número:"))
    
    if opcao == 10:
        break
print(opcao)
'''

'''
for numero  in range(100):
            
    if numero == 12:
        break
    print(numero, end=" ")

'''

''''
for numero  in range(100):
   if numero % 2 == 0:
      continue # o continue ele pula a execução  
   print(numero, end=" ")
'''


              