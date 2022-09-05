def generarMultiplos(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7
        numero+=1

obtieneMultiplo7 = generarMultiplos(10)
#print(obtieneMultiplo7)

# for n in obtieneMultiplo7:
#     print(n)

# print(next(obtieneMultiplo7))
# print("Aca hay 300 lineas de codigo...")
# print(next(obtieneMultiplo7))
# print("Aca hay 1000 lineas de codigo...")
# print(next(obtieneMultiplo7))