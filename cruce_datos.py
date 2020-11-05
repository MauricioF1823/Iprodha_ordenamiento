import sqlite3 as sq


def conexion():
    try:
        con = sq.connect('hoja_ruta_202010.db')
        return con

    except Exception as e:
        print(type(e))


def mostrar_datos():
    conI = conexion()
    cursosrI = conI.cursor()
    cursosrI.execute('SELECT DNITIT, CHACRA_ADM, DIRECCION_POSTAL, CLAVE_DISTRIBUCION From hoja_ruta')
    rows = cursosrI.fetchall()
    for row in rows:
        print(row)
    conI.close()


if __name__ == "__main__":
    mostrar_datos()

