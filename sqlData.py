import sqlite3

class DadosBanco():

    #INICIA A CONEXÃO COM O BANCO DE DADOS NA INICIALIZAÇÃO DA CLASSE
    def __init__(self):
        self.con = sqlite3.connect("banco.db")
        self.cursor = self.con.cursor()

    #CRIA A TABELA CASO A MESMA NÃO EXISTA
    def criarTabelaDB(self):
        try:
            self.cursor.execute('''SELECT CONTA FROM CLIENTE''')
        except sqlite3.OperationalError:
            self.cursor.execute('''CREATE TABLE CLIENTE (CONTA INTEGER,
            SALDO INTEGER)''')
            self.con.commit()
    
    def carregarDadosCliente(self):
        contas = self.cursor.execute('''SELECT * FROM CLIENTE''').fetchall()
        clientes = []
        for conta in contas:
            individuo = {'conta': conta[0], 'saldo': conta[1]}
            clientes.append(individuo)
        return clientes
          

    def escreverDadosCliente(self, vetor_contas):
        for conta in vetor_contas:
            try:
                self.cursor.execute('''UPDATE CLIENTE SET SALDO = {} WHERE CONTA = {}'''.format(conta.saldo, conta.numero))
            except:
                self.cursor.execute('''INSERT INTO CLIENTE VALUES ({}, {})'''.format(conta.numero, conta.saldo))
        self.con.commit()     


    #ENCERRA A CONEXÃO COM O BANCO DE DADOS
    def fecharConexaoDB(self):
        self.cursor.close()
        self.con.close()


    