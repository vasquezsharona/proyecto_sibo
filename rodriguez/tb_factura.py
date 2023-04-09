import sqlite3
with sqlite3.connect('E:\Vasquez\BDsibo')as con:
    micursor=con.cursor()
    sentencia="SELECT * FROM factura"
    print(micursor.execute(sentencia).fetchall())

def modificar(connetc,tabla,campo,dato,id_factura):
    micursor=connetc.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id_factura ='{id_factura}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa')
'''modificar(con,'factura','',)'''

def eliminar (connetc,tabla,campo,dato,id_factura):
    micursor=connetc.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa')
'''eliminar(con,'factura')'''

def insertar(id_factura,,id_reservas,fecha_emision,subtotal,impuestos,total):
    micursor=connetc.cursor()
    sentencia=f"INSERT INTO factura VALUES ({id_factura},'{id_reservas}','{fecha_emision}','{subtotal}','{impuestos}','{total})"
    micursor.execute(sentencia)
    con.commit()
    print('Agregacion exitosa')
    '''insertar()'''

    def leer():
        micursor=con.cursor()
        sentencia=f"SELECT * FROM factura"
        micursor.execute(sentencia)
        datos=micursor.fetchall()
        con.commit()
        print(datos)

    leer()