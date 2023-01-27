import mysql.connector

class DadosBanco():

    #INICIA A CONEXÃO COM O BANCO DE DADOS NA INICIALIZAÇÃO DA CLASSE
    def __init__(self):
        self.con = mysql.connector.connect(user='sql10593804',
                              password='vPTeIGmm67',
                              host='sql10.freemysqlhosting.net',
                              port=3306,
                              database='sql10593804')
        self.cursor = self.con.cursor()

    #CRIA A TABELA CASO A MESMA NÃO EXISTA
    def criarTabelaDB(self):
        try:
            self.cursor.execute('''CREATE TABLE CLIENTE (CONTA INT(3),
                                SALDO INT(10))''')
            self.con.commit()
        except mysql.connector.errors.ProgrammingError:
            pass
    
    def carregarDadosCliente(self):
        self.cursor.execute('''SELECT * FROM CLIENTE''')
        contas = self.cursor.fetchall()
        clientes = []
        for conta in contas:
            individuo = {'conta': conta[0], 'saldo': conta[1]}
            clientes.append(individuo)
        return clientes
       
    def escreverDadosCliente(self, vetor_contas):
        for conta in vetor_contas:            
            self.cursor.execute('''SELECT CONTA FROM CLIENTE 
                                WHERE CONTA = {}'''.format(conta.numero))
            contaExiste = self.cursor.fetchone()
            
            if contaExiste:
                self.cursor.execute('''UPDATE CLIENTE SET SALDO = {} 
                                    WHERE CONTA = {}'''.format(conta.saldo, conta.numero))
            else:
                 self.cursor.execute('''INSERT INTO CLIENTE 
                                    VALUES ({}, {})'''.format(conta.numero, conta.saldo))
            
        self.con.commit()     

    #ENCERRA A CONEXÃO COM O BANCO DE DADOS
    def fecharConexaoDB(self):
        self.cursor.close()
        self.con.close()


    