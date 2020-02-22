import pyodbc


def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from produto")
    for row in cursor:
        print(f'row = {row}')
    print() 

def create (conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute('insert into produto(nome,preco,qtd) values(?,?,?);',('manteiga', 5.67, 4))
    conn.commit()
    read(conn)


conn = pyodbc.connect(
    "Driver={SQL SERVER Native Client 11.0};"
    "Server=vaio;"
    "Database=loja;"
    "Trusted_Connection=yes;"
)       


read(conn)
create(conn)
conn.close()