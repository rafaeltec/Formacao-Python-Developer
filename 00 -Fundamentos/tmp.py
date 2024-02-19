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










frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)
        
        
pessoas_idades = {"Alice": 30, "Bob": 25, "Charlie": 35}
for nome, idade in pessoas_idades.items():
    print(f"{nome} tem {idade} anos")


 
opcao = 1

while opcao != 0:
    opcao = int (input("informe um número:"))
    
    if opcao == 10:
        break
print(opcao)






              