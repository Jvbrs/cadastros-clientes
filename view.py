import sqlite3 as lite

con = lite.connect('dados.db')





#inserindo dados
def inserir_cadastro(i):
    with con: 
        cur = con.cursor()
        query = "INSERT INTO dados(nome, idade, turno, endereço, data_de_entrada, data_de_saida, ultimo_pagamento, contato_responsavel, observacoes) VALUES(?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


#atualizar dados
def atualizar_dados(i):    
    with con: 
        cur = con.cursor()
        query = "UPDATE dados SET nome=?, idade=?, turno=?, endereço=?, data_de_entrada=?, data_de_saida=?, ultimo_pagamento=?, contato_responsavel=?, observacoes=?  WHERE id=?"
        cur.execute(query, i)
    
#deletar dados
def deletar_dados(i):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM dados WHERE id=?"
        cur.execute(query, i)



#ver dados

def ver_dados():
    ver_dados = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM dados"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


#ver dados individual
def ver_cliente(id):
    ver_dados_individual = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM dados WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual

