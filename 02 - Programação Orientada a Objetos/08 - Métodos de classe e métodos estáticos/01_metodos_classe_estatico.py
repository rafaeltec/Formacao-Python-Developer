# Classe Pessoa
class Pessoa:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome   # Nome da pessoa
        self.idade = idade # Idade da pessoa

    # Método de classe para criar um objeto Pessoa a partir da data de nascimento
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano  # Calcula a idade baseada no ano atual (2022)
        return cls(nome, idade)  # Retorna uma instância da classe com nome e idade calculada

    # Método estático para determinar se uma pessoa é maior de idade
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18  # Retorna True se idade for 18 ou mais, False caso contrário

# Cria um objeto Pessoa utilizando o método de classe
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
# Imprime o nome e a idade da pessoa
print(p.nome, p.idade)

# Usa o método estático para verificar a maioridade
print(Pessoa.e_maior_idade(18))  # True, 18 é maior de idade
print(Pessoa.e_maior_idade(8))   # False, 8 não é maior de idade
