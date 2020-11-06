import sqlite3 as sq


def conexion_iprodha():
    try:
        con = sq.connect('hoja_ruta_202010.db')
        return con

    except Exception as e:
        print(type(e))


def conexion_samsa():
    try:
        con = sq.connect('padron_2020.db')
        return con

    except Exception as e:
        print(type(e))


def mostrar_datos():
    con_i = conexion_iprodha()
    con_s = conexion_samsa()

    cursosrI = con_i.cursor()
    cursorS = con_s.cursor()

    cursosrI.execute('SELECT NOMBRE, CHACRA_ADM, DIRECCION_POSTAL, CLAVE_DISTRIBUCION From hoja_ruta')
    cursorS.execute('SELECT APELLIDOYNOMBRE, CALLEPOSTAL, NROPOSTAL, CAMINANTE, POSICION from padron_2020')

    beneficiarios_irpodha = cursosrI.fetchall()
    usuarios_samsa = cursorS.fetchall()

    for beneficiario in beneficiarios_irpodha:
        for usuario in usuarios_samsa:
            if beneficiario[0] == usuario[0]:
                print("Resultado:")

                print("Irpodha: ", beneficiario)
                print("Samsa:   ", usuario)
                x = input()

    con_i.close()
    con_s.close()


if __name__ == "__main__":
    mostrar_datos()

