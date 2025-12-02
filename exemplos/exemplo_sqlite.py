import sqlite3

def pedir_estudiante():
    '''Pide nome e idade dun estudiante e devólveos en forma de secuencia'''
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    #en este caso, en forma de tupla. Valdría una lista perfectamente
    return nombre, edad


def limpar_datos(cursor: sqlite3.Cursor):
    sql = "DROP TABLE IF EXISTS Estudiantes" 
    cursor.execute(sql)
    cursor.connection.commit()


#Creamos ou abrimos a base de datos SQLite
#Ollo á ruta: Os directorios intermedios deben existir dende a ruta de execución do script
with sqlite3.connect("exemplos//databases//bdd_exemplo.db") as conexion:
    
    #Creamos un cursor para facer as operacions
    mi_cursor = conexion.cursor()
    print("Conectado coa base de datos!")

    #limpo os datos para partir dende cero en cada proba
    limpar_datos(mi_cursor)

    #Engadimos unha nova táboa se non existe xa
    sql_table_estudiantes = """
    CREATE TABLE IF NOT EXISTS Estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    );
    """
    
    #executamos o CREATE TABLE
    mi_cursor.execute(sql_table_estudiantes)
    # Calquera operación de escritura (CREATE, UPDATE, INSERT, DELETE) debe ser confirmada con commit()
    # Co uso de with para abrir a conexión poderíamos obvialo (faise automáticamente todo antes de pechar)
    conexion.commit()

    # INSERTS
    # 1 - Alta dun estudante sen parametrizar valores
    sql_insert = """
        INSERT INTO Estudiantes (nombre, edad) 
        VALUES ('Pete Sampras', 45);
    """
    mi_cursor.execute(sql_insert)
    #sen with faríamos o commit

    #2 - Alta dun estudiante de valores recollidos, 
    # pero sen "asegurar" a consulta (Non recomendado -> perigo de SQL Injection)
    nombre, edad = pedir_estudiante()
    sql_insert = f"""
        INSERT INTO Estudiantes (nombre, edad) 
        VALUES ('{nombre}', {edad});
    """
    mi_cursor.execute(sql_insert)

    #3 - Alta dun estudiante parametrizando, asegurando a consulta con SQL parametrizado (con marcadores)
    #Los recojo como secuencia (tupla en este caso), para usarlos directamente 
    datos_estudiante = pedir_estudiante()
    sql_insert_param = """
        INSERT INTO Estudiantes (nombre, edad) 
        VALUES (?, ?);
    """
    mi_cursor.execute(sql_insert_param, datos_estudiante)

    #4 - Agora, inserto varios estudiantes con executemany()
    # pasamos os datos coma un iterable (listado dos estudiantes) de iterables (datos individuais de cada estudiante)
    #  Ex: lista de tuplas, lista de listas, ....
    # Pido dous para este exemplo 
    estudiante1 = pedir_estudiante()
    estudiante2 = pedir_estudiante()

    lista_estudiantes = [estudiante1, estudiante2]
    #Aproveito o sql parametrizado anterior. Realmente non hai cambios para este
    mi_cursor.executemany(sql_insert_param, lista_estudiantes)

    # SELECT
    sql_todos = "SELECT * FROM estudiantes"
    mi_cursor.execute(sql_todos)

    #Agora temos que ir extraíndo (fetch) os rexistros devoltos pola consulta
    #Podemos usar fetchall(), fetchone() ou fetchmany(). Avanzan unha especie de puntero de lectura
    clase_completa = mi_cursor.fetchall()


    print("VALORES DE LA TABLA")
    for estudiante in clase_completa:
        #estudiante será una tupla con los dos valores: nombre y edad
        print(estudiante)








    