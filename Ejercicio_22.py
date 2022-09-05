numero1 = 20
numero2 = 2

try:
    resultado = numero1 / numero2

except ZeroDivisionError:
    print("No se puede dividir entre 0...")
finally:
    print("Yo siempre aparezco")

print("Aqui termina el programa")