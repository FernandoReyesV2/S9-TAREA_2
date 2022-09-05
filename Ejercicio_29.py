class Persona():
    def __init__(self,apePat, apeMat, nom):
        self.apellidosPaternos = apePat
        self.apellidosMaternos = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{} {}, {}"
        return txt.format(self.apellidosPaternos,self.apellidosMaternos,self.nombres)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Persona):
    def __init__(self,apePat, apeMat, nom,pro):
        super().__init__(apePat,apeMat,nom)
        self.profesion = pro

    def datos(self):
        super().datos()
        print("Profesion: ",self.profesion)

# per1= Persona2 ("Torres","Lopez","Juan")
# estu1= Estudiante("Torres","Lopez","Juan","Ingenieria Civil")
# print(estu1.mostrarNombreCompleto())
# print(estu1.profesion)
# estu1.datos()
# print(isinstance(per1,Estudiante))