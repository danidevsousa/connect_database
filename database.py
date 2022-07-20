import mysql.connector 
from mysql.connector import Error
try:
    con = mysql.connector.connect(host='localhost',database='foo',user='root',password='admin')

    inserir_produtos = """INSERT INTO produtos
        (idProduto, NomeProduto, Preco, Quantidade) VALUES 
        (1, "Camera", 120.00, 2),
        (2, "Mouse", 150.00, 5),
        (3, "Lapiseira", 2.00, 2),
        (4, "Teclado", 180.00, 3)
        """
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registros adicionados com sucesso!")
    cursor.close()
except Error as erro:
    print(f"Falha ao inserir dados no MYSQL: {erro}")     
finally:
    if (con.is_connected()):
        con.close()
        print("Conexão ao MySQL foi encerrada")


