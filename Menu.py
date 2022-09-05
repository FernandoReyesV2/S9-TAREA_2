from Ejercicio_1 import *
from Ejercicio_2 import *
from Ejercicio_3 import *
from Ejercicio_4 import *
from Ejercicio_5 import *
from Ejercicio_6 import *
from Ejercicio_7 import *
from Ejercicio_8 import *
#from Ejercicio_9 import *
#from Ejercicio_10 import *
from Ejercicio_11 import *
from Ejercicio_12 import *
from Ejercicio_13 import *
from Ejercicio_14 import *
#from Ejercicio_15 import *
#from Ejercicio_16 import *
#from Ejercicio_17 import *
#from Ejercicio_18 import *
# from Ejercicio_19 import *
from Ejercicio_20 import *
from Ejercicio_21 import *
#from Ejercicio_22 import *
from Ejercicio_23 import *
from Ejercicio_24 import *
from Ejercicio_25 import *
from Ejercicio_26 import *
from Ejercicio_27 import *
from Ejercicio_28 import *

from Ejercicio_30 import ClaseA,ClaseB,ClaseX
from Ejercicio_31 import *
from Ejercicio_32 import *

print("Menu Principal")
menu = int(input("Digite la opcion del 1 al 32: "))
while menu != 0:
    if menu == 1:
        print(nombre, edad, sueldo, boolean)
        input("---Presione una tecla para continuar---")
    elif menu == 2:
        print("Suma num1 + num2 35 + 18",numero1 + numero2)
        print("Suma num1 + num2 35 + 28",num1 + num2)
        print ("Sueldo", sueldoEntero )
        print("Valor decimal",valorDecimal * 3)
        print("Len de edad",len(str(edad)))
        input("---Presione una enter para continuar---")
    elif menu == 3:
        print("Suma: ", num1 + num2)
        print("Resta: ", num1 - num2)
        print("Multiplicacion: ", num1 * num2)
        print("Division: ", num1 / num2)
        print("Division Exacta: ", num1 // num2)
        print("Potencia: ", num1 ** num2)
        input("---Presione una enter para continuar---")
    elif menu == 4:
        print(textoFinal)
        print("El saludo es : %s %s" % (texto1, texto2))
        print(saludoFinal)
        print(saludoFinal2)
        input("---Presione una enter para continuar---")
    elif menu == 5:
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())
        print(texto.find("al"))
        print(texto.count("e"))
        print(textoFinal)
        print(valor)
        print(cadenaSeparada)
        input("---Presione una enter para continuar---")
    elif menu == 6:
        print(tupla,tupla2,tupla3)
        print(tupla3[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])
        print(a)
        print(b)
        print(c)
        print(tuplaFinal)
        print(tuplaFinal.count(21))
        print(tuplaFinal.index(3))
        input("---Presione una enter para continuar---")
    elif menu == 7:
        print(lista1)
        print(lista1[:1])
        print(lista1[2])
        print(lista1[-1])
        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])
        print(lista1)
        print(lista1.index("Flavio"))
        print(lista3)
        print(lista2 * 4)
        print("UskoKrun2022410" in lista1)
        input("---Presione una enter para continuar---")
    elif menu == 8:
        print(miDiccionario)
        print(dic2[25])
        print(dicPaises)
        print(datosPersonales)
        print(datosPersonales["Anios"])
        print(datosPersonales.get("Apellido", "Oscar"))
        print(datosPersonales.keys())
        print(valores)
        input("---Presione una enter para continuar---")
    elif menu == 9:
        nombre = input(" Ingrese su nombre : ")
        edad = int(input(" Ingrese su edad : "))
        sueldo = float(input(" Ingrese su sueldo : "))
        edadFutura = edad + 20
        print(" Hola, ", nombre)
        print(" Tu edad es : ", edad)
        print(" Tu edad ( dentro de 20 años ) será : ", edadFutura)
        print(" Tu sueldo es : ", sueldo)
        input("---Presione una enter para continuar---")
    elif menu == 10:
        edad = int(input("Ingrese su edad: "))
        if edad > 18:
            print("Eres mayor de edad")
        elif edad == 18:
            print("Tines 18 años")
        else:
            print("No eres mayor de 18 años")
        input("---Presione una enter para continuar---")
    elif menu == 11:
        print("Garcia")
        print("Oscar")
        print("Uskokrun2010")
        print(saludar())
        evaluarSueldoMinimo(860)
        input("---Presione una enter para continuar---")
    elif menu == 12:
        print(not tieneBeneficio)
        input("---Presione una enter para continuar---")
    elif menu == 13:
        print(sexo)
        print(sexo1)
        input("---Presione una enter para continuar---")
    elif menu == 14:
        print(numeros[1])
        print(numeros1[5])
        print(numeros2[9])
        input("---Presione una enter para continuar---")
    elif menu == 15:
        for i in range(1, 12):
            print("{0} * {1} es: {2}".format(i, i, (i * i)))

        for num in ["Karen", "Oscar", "Hector", "Leonardo"]:
            print("Cantidad de letras de {0} es: {1}".format(num, len(num)))
        input("---Presione una enter para continuar---")
    elif menu == 16:
        print("---Cursos---")
        print("Matematicas - Biologia - Lenguaje - Ciencias")
        curso = input("Ingrese el curso deseado: ")

        if curso in ("MatematicaS", "Biologia", "Leanguaje", "Ciencias"):
            print("Curso {0} seleccionado".format(curso))
        else:
            print("No existe ese curso")
        input("---Presione una enter para continuar---")
    elif menu == 17:
        input("---Presione una enter para continuar---")
        numero = int(input("Ingrese un numero: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
        print("El factorial de {} es {}".format(numero, factorial))
    elif menu == 18:
        indice = 1
        while indice < 10:
            print("Valor actual {}".format(indice))
            indice = indice + 1

        print("Hemos terminado el bucle while")

        inicio = 2

        while inicio <= 100:
            print("Numero par: ", inicio)
            inicio += 2

        print("Hemos terminado el bucle while")
        input("---Presione una enter para continuar---")
    elif menu == 19:
        for numero in range(1, 6):
            if numero == 3:
                break
            print("El numero es: ", numero)

        print("Bucle terminado")

        for numero in range(1, 6):
            if numero == 3:
                continue
            print("El numero es: ", numero)

        print("Bucle terminado")

        for numero in range(1, 6):
            if numero <= 3:
                pass
            else:
                print("El siguiente valor es mayor a 3")
            print("El numero es: ", numero)

        print("Bucle terminado")
        input("---Presione una enter para continuar---")
    elif menu == 20:
        print(next(obtieneMultiplo7))
        print("Aca hay 300 lineas de codigo...")
        print(next(obtieneMultiplo7))
        print("Aca hay 1000 lineas de codigo...")
        print(next(obtieneMultiplo7))
        input("---Presione una enter para continuar---")
    elif menu == 21:
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        input("---Presione una enter para continuar---")
    elif menu == 22:
        numero1 = 20
        numero2 = 2
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print("No se puede dividir entre 0...")
        finally:
            print("Yo siempre aparezco")

        print("Aqui termina el programa")
        input("---Presione una enter para continuar---")
    elif menu == 23:
        evaluarNota(19)
        input("---Presione una enter para continuar---")
    elif menu == 24:
        print(sumar(5, 6))
        print(multiplicar(5, 6))
        input("---Presione una enter para continuar---")
    elif menu == 25:
        print(multiplicar(5, 6))
        print(contarLetras("uskokrum2010"))
        input("---Presione una enter para continuar---")
    elif menu == 26:
        persona1 = Persona()
        persona1.apellidos = "Garcia Fuentes"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)
        input("---Presione una enter para continuar---")
    elif menu == 27:
        curso1 = Curso("Matematica", 5, "Ingenieria civil")
        print(curso1)
        curso1.mostrarDatos()
        input("---Presione una enter para continuar---")
    elif menu == 28:
        cuenta1 = Cuenta("oscar Garcia", 1500, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dolares")
        print(cuenta1.get_Moneda())
        input("---Presione una enter para continuar---")
    elif menu == 29:
        from Ejercicio_29 import Persona, Estudiante
        per1 = Persona("Torres", "Lopez", "Juan")
        estu1 = Estudiante("Torres", "Lopez", "Juan", "Ingenieria Civil")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        estu1.datos()
        print(isinstance(per1, Estudiante))
        input("---Presione una enter para continuar---")
    elif menu == 30:
        cx1 = ClaseX()
        input("---Presione una enter para continuar---")
    elif menu == 31:
        doc1 = Trabajador()
        describirPersona(doc1)
        input("---Presione una enter para continuar---")
    elif menu == 32:
        pais1 = Pais("Peru", "Martin Vizcarra")
        print(pais1)

        ciudad1 = Ciudad("chiclayo", 15000, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("Maria de los angeles", ciudad1)
        print(urba1)
        input("---Presione una enter para continuar---")
    else:
        print("Opcion no valida")
    menu = int(input("Digite la opcion del 1 al 32 o escriba 0 para salir: "))