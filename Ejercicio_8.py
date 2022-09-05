miDiccionario = {"España": "Madrid", "Peru": "Lima","Alemania":"Berlin"}
# print("Peru")
# print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"
# print(miDiccionario)

miDiccionario["España"] = "Barcelona"
# print(miDiccionario)

del miDiccionario["España"]
# print(miDiccionario)

dic2 = {"Garcia": "Oscar",25:True,"Sueldo":150.60}
# print(dic2[25])

llaves = ("España","Francia","Inglaterra")
dicPaises = {llaves[0]: "Madrid", llaves[1]: "Paris", llaves[2]: "Londres"}
# print(dicPaises)

datosPersonales = {"Apellido" : "Garcia", "Anios":{1:2010,2:2011,3:2012,4:2013,5:2014}}
# print(datosPersonales)
# print(datosPersonales["Anios"])
#
# print(datosPersonales.get("Apellido","Oscar"))

# print(datosPersonales.keys())
valores = tuple (datosPersonales.values())
# print(valores)