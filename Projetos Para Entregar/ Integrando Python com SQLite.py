from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))
    
    # Relacionamento com a tabela Conta
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    saldo = Column(Numeric)
    
    # Relacionamento com a tabela Cliente
    cliente = relationship("Cliente", back_populates="contas")

# Criação do engine do SQLAlchemy para SQLite
engine = create_engine('sqlite:///banco.db')
Base.metadata.create_all(engine)

# Criando uma sessão para inserir e consultar dados
Session = sessionmaker(bind=engine)
session = Session()
# Inserindo dados na tabela Cliente
cliente1 = Cliente(nome="João Silva", cpf="123456789", endereco="Rua ABC, 123")
session.add(cliente1)

# Inserindo dados na tabela Conta
conta1 = Conta(tipo="corrente", agencia="0001", num=12345, saldo=2000.50, cliente=cliente1)
session.add(conta1)

session.commit()
# Recuperando todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente.nome, cliente.cpf, cliente.endereco)

# Recuperando todas as contas de um cliente
contas_do_joao = session.query(Conta).filter(Conta.cliente == cliente1).all()
for conta in contas_do_joao:
    print(conta.tipo, conta.agencia, conta.num, conta.saldo)
