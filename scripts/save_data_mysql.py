import os
from dotenv import load_dotenv
import mysql.connector

import pandas as pd

# Carrega as variáveis do arquivo .env no ambiente de trabalho
load_dotenv()


def connect_mysql(host_name, user_name, pw):

    # A função os.getenv é usada para obter o valor das variáveis de ambiente
    host = host_name
    user = user_name
    password = pw

    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    return cnx

def create_cursor(cnx):
    cursor = cnx.cursor()
    
    return cursor

def create_database(cursor, db_name):
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + db_name +";")

def show_databases(cursor):
    cursor.execute("SHOW DATABASES;")
    for db in cursor:
        print(db) 

def create_product_table(cursor, db_name, tb_name):
    
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS """ + db_name + "." + tb_name + """(
        id VARCHAR(100),
        Produto VARCHAR(100),
        Categoria_Produto VARCHAR(100),
        Preco FLOAT(10,2),
        Frete FLOAT(10,2),
        Data_Compra DATE,
        Vendedor VARCHAR(100),
        Local_Compra VARCHAR(100),
        Avaliacao_Compra INT,
        Tipo_Pagamento VARCHAR(100),
        Qntd_Parcelas INT,
        Latitude FLOAT(10,2),
        Longitude FLOAT(10,2),

        PRIMARY KEY (id)                  
        );
    """)

def show_tables(cursor, db_name):
    cursor.execute("USE " + db_name +";")
    
    cursor.execute("SHOW TABLES;")

    for tb in cursor:
        print(tb)

def read_csv(path):
    import pandas as pd

    file = pd.read_csv(path)

    return file

def add_product_data(cnx, cursor, df, db_name, tb_name):
    lista_dados =  [tuple(row) for i, row in df.iterrows()]
    sql = f"INSERT INTO {db_name}.{tb_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    cursor.executemany(sql, lista_dados)
    cnx.commit()
    print(cursor.rowcount, "dados foram inseridos.")

def drop_table(cursor, db_name, tb_name):    
    cursor.execute("DROP TABLE IF EXISTS " + db_name + "." +tb_name + ";")
    print(f"table {db_name}.{tb_name} droped successfully")

def show_table_nm_records(cursor, db_name, tb_name):
    # sql = "SELECT * FROM dbprodutos.tb_livros_2021;"
    sql = "SELECT COUNT(*) FROM " + db_name + "." + tb_name +";"

    cursor.execute(sql)
    print("Number of records is: ")
    for tb in cursor:
        print(tb)

if __name__ == "__main__":

    connection = connect_mysql(os.getenv("DB_HOST"), os.getenv("DB_USERNAME"), os.getenv("DB_PASSWORD"))
    cursor = create_cursor(connection)
       
    create_database(cursor, 'dbprodutos_test')
#   show_databases(cursor)
#   show_tables(cursor, 'dbprodutos_test')

    print("Creating Table IF NOT EXISTS")
    print("         ------            ")
    
    drop_table(cursor, 'dbprodutos_test', 'tb_livros')
    create_product_table(cursor, 'dbprodutos_test', 'tb_livros')
    
    show_tables(cursor, 'dbprodutos_test')

    df = read_csv("/home/fabiano/Projetos/pipeline-python-mongo-mysql/data/tabela_livros.csv")
    print(df.head())

    show_table_nm_records(cursor, 'dbprodutos_test', 'tb_livros')

    print("Adding CSV file data into table")
    
    add_product_data(connection, cursor, df, 'dbprodutos_test', 'tb_livros')

