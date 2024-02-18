
T = input("Rafael")

if len(T) > 10:
    print("MUTE")
else:
    print("TWEET")





def encaixa(A, B):
    # Verifica se os últimos dígitos de A correspondem a B
    return A[-len(B):] == B

# Entrada do usuário
N = int(input())

# Para cada caso de teste
for _ in range(N):
    A, B = input().split()
    
    # Verificando se B encaixa em A
    if encaixa(A, B):
        print("encaixa")
    else:
        print("nao encaixa")
