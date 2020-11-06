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
                # if usuario[1] in beneficiario[2]:
                print("Resultado:")
                print("Irpodha: ", beneficiario)
                print("Samsa:   ", usuario)
                x = input("Actualizar clave_distribución: s/n")
                if x == 's':
                    beneficiario[3] = usuario[3] + "-" + usuario[4]
                    print(beneficiario)
                    cursorS.execute('UPDATE hoja_ruta SET CLAVE_DISTRIBUCION=?'beneficiario[3]')


    con_i.close()
    con_s.close()


if __name__ == "__main__":
    mostrar_datos()
