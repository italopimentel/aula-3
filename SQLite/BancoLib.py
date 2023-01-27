import random
from sqlData import DadosBanco

class Conta():
    def __init__(self, numConta, saldo = 0):
        self.numero = numConta
        self.saldo = saldo

    def deposite(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.dados = DadosBanco()
        self.dados.criarTabelaDB()
        self.contas = []

    def carregarContas(self):
        clientes = self.dados.carregarDadosCliente()

        for cliente in clientes:
            self.contas.append(Conta(cliente['conta'], cliente['saldo']))
    
    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor)

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)
    
    def encerrarConexao(self):
        self.dados.escreverDadosCliente(self.contas)
        self.dados.fecharConexaoDB()
