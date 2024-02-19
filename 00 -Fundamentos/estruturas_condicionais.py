
MAIOR_IDADE = 18

idade = int(input("informe sua idade"))

if idade >= MAIOR_IDADE:
    print("Mairo de idade, pode tirara habilitação")
    
if idade < MAIOR_IDADE:
    print("Ainda nao pode, tirar a Cnh")
    
if idade >= MAIOR_IDADE:
    print("Mairo de idade, pode tirara habilitação")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

 # serve para comentar linha inteira enquanto 3 aspas ele comenta um escopo
 


