def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

lenguajesObtenidos = devuelveLenguajes("Python","Java","Php","Ruby","Javascript")

# print(next(lenguajesObtenidos))
# print(next(lenguajesObtenidos))