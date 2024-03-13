# Definição da classe Estudante
class Estudante:
    # Variável de classe, compartilhada por todas as instâncias
    escola = "DIO"

    # Método construtor
    def __init__(self, nome, matricula):
        self.nome = nome           # Variável de instância para o nome
        self.matricula = matricula # Variável de instância para a matrícula

    # Método especial para representar o objeto como string
    def __str__(self) -> str:
        # Retorna uma string formatada com nome, matrícula e escola
        return f"{self.nome} - {self.matricula} - {self.escola}"

# Função para mostrar os valores dos objetos Estudante
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)  # Chama __str__ de cada objeto Estudante

# Criação de duas instâncias de Estudante
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
# Mostra os valores de aluno_1 e aluno_2
mostrar_valores(aluno_1, aluno_2)

# Modificação da variável de classe 'escola'
Estudante.escola = "Python"
# Criação de uma nova instância de Estudante
aluno_3 = Estudante("Chappie", 3)
# Mostra os valores de aluno_1, aluno_2 e aluno_3
mostrar_valores(aluno_1, aluno_2, aluno_3)
