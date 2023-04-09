import sqlite3
with sqlite3.connect('E:\Vasquez\BDsibo')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM inventario"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_inventario):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_inventario ='{id_inventario}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa')
'''modificar(con,'inventario','',)'''

def eliminar (connetc,tabla,campo,dato,id_inventario):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa')
'''eliminar(con,'inventario')'''

def insertar(id_inventario,nombre,descripcion,cantidad,precio_unitario):
	micursor=connetc.cursor()
    sentencia=f"INSERT INTO factura VALUES ({id_inventario},'{descripcion}','{cantoidad}','{precio_unitario})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')
    '''insertar()'''

    def leer():
        micursor=con.cursor()
        sentencia=f"SELECT * FROM inventario"
        micursor.execute(sentencia)
        datos=micursor.fetchall()
        con.commit()
        print(datos)

    leer()