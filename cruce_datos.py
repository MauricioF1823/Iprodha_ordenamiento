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

    cursorI = con_i.cursor()
    cursorS = con_s.cursor()

    cursorI.execute('SELECT NOMBRE, CHACRA_ADM, DIRECCION_POSTAL, CLAVE_IPRODHA, CLAVE_DISTRIBUCION From hoja_ruta')
    cursorS.execute('SELECT APELLIDOYNOMBRE, CALLEPOSTAL, NROPOSTAL, CAMINANTE, POSICION from padron_2020')

    beneficiarios_irpodha = cursorI.fetchall()
    usuarios_samsa = cursorS.fetchall()

    for beneficiario in beneficiarios_irpodha:
        for usuario in usuarios_samsa:
            if beneficiario[0] == usuario[0]:
                # if usuario[1] in beneficiario[2]:
                print("Resultado:")
                print("Irpodha: ", beneficiario[0], beneficiario[2], beneficiario[1], " cam: ", str(beneficiario[4]))
                print("Samsa:   ", usuario)
                print(type(beneficiario[1]))

                print("1 - Actualizar clave distribucion con datos de samsa")
                print("2 - Asignar chacra adm")
                print("3 - Saltear")
                x = input("Ingrese una opcion: ")
                if x == '1':
                    clave_distri = str(usuario[3]) + "-" + str(usuario[4])
                    #print(clave_distri)
                if x == '2':
                    clave_distri = str(beneficiario[1])
                if x == '3':
                    pass

                if x == '1' or x == '2':
                    try:
                        cursorI.execute("""UPDATE hoja_ruta SET CLAVE_DISTRIBUCION=? where CLAVE_IPRODHA=?""", (clave_distri, beneficiario[3]))
                        con_i.commit()
                        print("Actualizacion con exito")
                    except Exception as e:
                        print(e)

    con_i.close()
    con_s.close()


if __name__ == "__main__":
    mostrar_datos()
