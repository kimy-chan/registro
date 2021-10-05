from werkzeug.security import generate_password_hash
registro = {
    "nombre": None,
    "usuario": None,
    "contraseña": None
}

boleano = True

while boleano:
    print ("1.registrarse \n 2.ingresar \n 3.ver usuarios registrados \n 4.borrar mi cuenta \n 5 editar\n 6.salir" )
    entrada = int(input(": "))
    if entrada == 1:
        print("registro")
        registro["nombre"] = input("nombre ")
        registro["usuario"] = input("usuarios ")
        contraseña = input("contraseña" )
        registro["contraseña"] = generate_password_hash(contraseña,'sha256')
    elif entrada == 2:
        user = input("ingrese su usuario ")
        contraseña = input("ingrese su contraseña ")
        if registro["nombre"] == None and registro["usuario"] == None and registro["contraseña"] == None:
            print ("la cuenta no existe")
        elif registro["usuario"] == user and registro["contraseña"]:
            print ("bienbenido "+ registro["nombre"])
        else:
            print ("contraseña incorrecta")
    elif entrada == 3:
        try:
            if registro["nombre"] == None and registro["usuario"] == None and registro      ["contraseña"]== None:
                print("no hay registros")
            else:
                print("usuarios registrados")
                for peer in registro.items():
                    print (peer)
        except KeyError:
            print("la cuenta fue borrada")
    elif entrada == 4:
        if registro["nombre"] == None and registro["usuario"] == None and registro["contraseña"] == None:
            print("la cuenta no existe")
        else:
            registro.clear()
            print("registro borrado")
    elif entrada == 5:
        try:
            if registro["nombre"] == None and registro["usuario"] == None and registro["contraseña"] == None:
                print("la cuenta no existe")
            else:
                print("editar registro")
                registro["nombre"] = input("nombre ")
                registro["usuario"] = input("usuarios ")
                registro["contraseña"] = input("contraseña ")
        except KeyError:
            print("la cuenta fue borrada")
    elif entrada == 6:
        boleado = False
        break
