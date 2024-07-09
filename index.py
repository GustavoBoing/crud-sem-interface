import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Guga2803",
    database = "bd_crud",
)

cursor = conexao.cursor() #para iniciar o crud

#CRUD

# CREATE
nome_produto = "Mouse Gamer"
valor_produto = 89
comando = f'INSERT INTO vendas(nome_produto, valor_produto) VALUES ("{nome_produto}", {valor_produto})'
cursor.execute(comando)
#conexao.commit() # utilizar quando o codigo modifica o banco de dados


# READ
comando = f'SELECT * FROM vendas'
resultado = cursor.fetchall() #ler o banco de dados
#print(resultado)

# UPDATE
nome_produto = "Cadeira "
idvendas = 4
comando = f'UPDATE vendas SET nome_produto = "{nome_produto}", valor_produto = 399 WHERE idvendas = {idvendas}'
cursor.execute(comando)
#conexao.commit() # utilizar quando o codigo modifica o banco de dados

# DELETE
nome_produto = "Teclado"
idvendas = 2
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # utilizar quando o codigo modifica o banco de dados

cursor.close() # finalizar o crud
conexao.close() # finalizar o crud