def numero_para_mes(numero):
    meses = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return meses.get(numero)

# Entrada do usuário
numero = int(input())

# Convertendo o número para o nome do mês correspondente
nome_mes = numero_para_mes(numero)

# Imprimindo o nome do mês
print(nome_mes)
