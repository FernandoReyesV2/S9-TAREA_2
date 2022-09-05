def evaluarNota(nota):
    if nota < 0:
        raise ValueError("Valor incorrecto...")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")

# evaluarNota(19)