import sqlite3
with sqlite3.connect('E:\Vasquez\BDsibo')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM habitacion"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_habitacion):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_habitacion ='{id_habitacion}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa')
'''modificar(con,'habitacion','',)'''

def eliminar (connetc,tabla,campo,dato,id_habitacion):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa')
'''eliminar(con,'habitacion')'''

def insertar(id_habitacion,tipo_habitacion,precio_noche,descripcion):
    micursor=connetc.cursor()
    sentencia=f"INSERT INTO factura VALUES ({id_habitacion},'{tipo_habitacion}','{precio_noche}','{descripcion})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')
    '''insertar()'''

    def leer():
        micursor=con.cursor()
        sentencia=f"SELECT * FROM habitacion"
        micursor.execute(sentencia)
        datos=micursor.fetchall()
        con.commit()
        print(datos)

    leer()