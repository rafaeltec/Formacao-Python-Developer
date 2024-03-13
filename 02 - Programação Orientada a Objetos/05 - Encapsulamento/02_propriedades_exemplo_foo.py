# Classe Foo
class Foo:
    # Método construtor
    def __init__(self, x=None):
        self._x = x  # Atributo privado _x

    # Decorador property, definindo um getter para x
    @property
    def x(self):
        # Retorna _x se ele não for None, caso contrário retorna 0
        return self._x or 0

    # Decorador setter para x
    @x.setter
    def x(self, value):
        # Incrementa _x pelo valor fornecido
        # Cuidado: isso gera erro se _x for inicialmente None
        self._x += value

    # Decorador deleter para x
    @x.deleter
    def x(self):
        # Redefine _x para 0
        self._x = 0

# Criando uma instância de Foo com _x inicializado como 10
foo = Foo(10)
# Imprimindo o valor de x (que chama o getter)
print(foo.x)  # Saída: 10

# Deletando x (chama o deleter que redefine _x para 0)
del foo.x
# Imprimindo o valor de x novamente
print(foo.x)  # Saída: 0

# Atribuindo 10 a x (chama o setter que incrementa _x por 10)
# Mas como _x era 0, agora será 10
foo.x = 10
# Imprimindo o valor de x mais uma vez
print(foo.x)  # Saída: 10
