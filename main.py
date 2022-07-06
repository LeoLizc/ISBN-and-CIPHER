#Programa principal.

import os
import Cesar
import Vigenere
import ISBN

print("BIENVENIDO A: MÉTODOS DE CIFRADO\n")
opcionabc = input(
    "Ingrese que alfabeto desea usar:\n+ Español (ñ)\n+ Inglés (e)\n+ Otro (o)\n>"
).upper()
if opcionabc == "Ñ":
    Cesar.alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
elif opcionabc == "E":
    Cesar.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
elif opcionabc == "O":
    Cesar.alfabeto = input("Ingrese su alfabeto:\n>").upper()

algo = -1
while algo != 0:
    algo = -1

    switch = -1
    print(
        "\n¿Qué algoritmo desea usar?:\n+ Cifrado de César (1)\n+ Cifrado de Vigenère (2)\n+ ISBN (3)\n+ Salir (0)"
    )
    while algo < 0 or algo > 3:
        try:
            algo = int(input(">"))
        except:
            pass

    if algo == 1:
        print(
            "\t¿Qué desea hacer?:\n\t+ Cifrar mensaje (1)\n\t+ Descifrar mensaje (2)"
        )
        while switch < 1 or switch > 2:
            try:
                switch = int(input("\t>"))
            except:
                pass
        if switch == 1:

            texto = input("\t\tMensaje a cifrar > ")
            n = 0
            print("\t\tIngrese n (n ≠ 0)")
            while n == 0:
                try:
                    n = int(input("\t\t>"))
                except:
                    pass
            print("\t\tEl mensaje cifrado es:\n\t\t>" + Cesar.cesar(texto, n))

        elif switch == 2:  #CÉSAR
            texto = input("\t\tMensaje cifrado > ")
            switch2 = -1
            print(
                "\t\tElija un tipo de descifrado:\n\t\t+ Descifrar dando n (1)\n\t\t+ Descifrar de forma avanzada (2)"
            )

            while switch2 < 1 or switch2 > 2:
                try:
                    switch2 = int(input("\t\t>"))
                except:
                    pass

            if switch2 == 1:
                n = 0
                print("\t\tIngrese n (n ≠ 0)")
                while n == 0:
                    try:
                        n = int(input("\t\t>"))
                    except:
                        pass
                print("\t\tEl mensaje descifrado es:\n\t\t>" +
                      Cesar.cesar(texto, -n))

            elif switch == 2:
                #PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM
                print(
                    "\t\tIngrese la letra de mayor frecuencia en el idioma (inglés --> 'e')"
                )
                freq = ''

                while not freq.isalpha():
                    freq = input("\t\t>")

                print("\t\tEl mensaje descifrado es:\n\t\t>" +
                      Cesar.cesar(texto, 0, freq))

    elif algo == 2:  #VIGENERE
        print(
            "\t¿Qué desea hacer?:\n\t+ Cifrar mensaje (1)\n\t+ Descifrar mensaje (2)\n\t+ Cifrar mensaje con el codigo del grupo(3)\n\t+ decifrar mensaje con el codigo del grupo(4)"
        )
        while switch < 1 or switch > 4:
            try:
                switch = int(input("\t>"))
            except:
                pass

        if switch == 1:
            texto = input("\t\tMensaje a cifrar > ")
            cl = ""
            while not cl.isalpha():
                cl = input("\t\tIngrese clave > ")

            print("\t\tEl mensaje cifrado es:\n\t\t>" +
                  Vigenere.vigenere(texto, cl))
        if switch == 2:
            texto = input("\t\tMensaje a descifrar > ")
            cl = ""
            while not cl.isalpha():
                cl = input("\t\tIngrese clave > ")

            print("\t\tEl mensaje descifrado es:\n\t\t>" +
                  Vigenere.vigenere(texto, cl, False))
        if switch == 3:
            texto = input("\t\tMensaje a cifrar > ")
            print("\t\tEl mensaje descifrado es:\n\t\t>" +
                  Vigenere.vigenere(texto, "grupotres"))
            cod1 = Vigenere.vigenere(texto, "grupotres")

        elif switch == 4:
            grupo3 = "grupotres"
            cont = 0
            cclave = ""
            salir = False
            while not salir and cont < 3:
                cclave = input("\t\tInserte la clave: ")
                if cclave == grupo3:
                    salir = True
                    print("\t\tEl mensaje descifrado es:\n\t\t>" +
                          Vigenere.vigenere(cod1, "grupotres", False))
                else:
                    cont = cont + 1
                    print("te quedan ", (3 - cont), ' intentos')

            if not salir: print("BLOQUEADO, la clave era 'grupotres'")

    elif algo == 3:  #ISBN
        #9789584216601
        print(
            "\t¿Qué desea hacer?:\n\t+ Arreglar código (1)\n\t+ Encontrar título por código (2)\n\t+ Verificar si el código es ISBN (3)"
        )
        while switch < 1 or switch > 3:
            try:
                switch = int(input("\t>"))
            except:
                pass

        codigo = input("\t\tDigite código > ")

        if switch == 1:
            pos = -1
            l = len(codigo)
            print("\t\tDigite posición de error [0, " + str(l) + ")")
            while pos < 0 or pos >= l:
                try:
                    pos = int(input("\t\t>"))
                except:
                    pass

            isbn = ISBN.solucionar_ISBN(codigo, pos)
            if isbn == None:
                print(
                    "\t\tEl código no pudo ser arreglado o no corresponde al código de un libro."
                )
            else:
                print("\t\tEl código arreglado es:", isbn)

        elif switch == 2:
            print(ISBN.titulo_ISBN(codigo))
        elif switch == 3:
            print("El código " + codigo +
                  ("" if ISBN.es_ISBN(codigo) else " NO") +
                  " corresponde a un código ISBN")

    elif algo == 0:
        print("\nGracias por usar el sistema! Que tenga un buen día.")
        break

    input("\n[Enter] para continuar")
    os.system('cls' if os.name == 'nt' else 'clear')
