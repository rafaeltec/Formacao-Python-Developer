# Classe Pessoa
class Pessoa:
    # Método construtor
    def __init__(self, nome, ano_nascimento):
        self.nome = nome                     # Nome público da pessoa
        self._ano_nascimento = ano_nascimento  # Ano de nascimento privado (indicado pelo underscore)

    # Decorador property para criar uma propriedade 'idade'
    @property
    def idade(self):
        _ano_atual = 2022  # Ano atual definido estaticamente
        # Calcula e retorna a idade
        return _ano_atual - self._ano_nascimento

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Guilherme", 1994)
# Imprimindo nome e idade da pessoa
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
