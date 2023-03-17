import sqlite3 as lite

#conexão com bd
con = lite.connect('dados.db')

#criação tablea

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE dados(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade DECIMAL,turno TEXT, endereço TEXT, data_de_entrada DATE, data_de_saida DATE, ultimo_pagamento DATE, contato_responsavel TEXT, observacoes TEXT)")
