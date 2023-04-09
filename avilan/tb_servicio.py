import sqlite3
with sqlite3.connect('E:\Vasquez\BDsibo')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM servicios"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_servicios):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_servicios ='{id_servicios}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa')
'''modificar(con,'servicios','',)'''

def eliminar (connetc,tabla,campo,dato,id_servicios):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa')
'''eliminar(con,'servicios')'''

def insertar(id_servicio,nombre,descripcion,cantidad,precio_unitario):
    micursor=connetc.cursor()
    sentencia=f"INSERT INTO factura VALUES ({id_servicio},'{nombre}','{descripcion}','{cantidad}','{precio_unitario})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')
    '''insertar()'''

    def leer():
        micursor=con.cursor()
        sentencia=f"SELECT * FROM servicio"
        micursor.execute(sentencia)
        datos=micursor.fetchall()
        con.commit()
        print(datos)

    leer()