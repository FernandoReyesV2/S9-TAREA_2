class Curso():
    def __init__(self,nom,cre,pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "presencial" #Propiedad encapsulada

    def mostrarDatos(self):
        dat = "Nombre: {} / Creditos: {} / Modo de imparticion: {}"
        print(dat.format(self.nombre,self.creditos,self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        if docenteAsignado:
            print("Existe docente asigando")
        else:
            print("No es necesario asignar un docente...")

    def __verificarDocente(self):
        # print("Vericando si existe un docente asignado...")
        if self.__imparticion == "presencial":
            return True
        else:
            return False

    def __str__(self):
        texto = "nombre: {} - creditos: {}"
        return texto.format(self.nombre,self.creditos)

# curso1 = Curso("Matematica",5,"Ingenieria civil")
# print(curso1)
# curso1.mostrarDatos()


# curso2 = Curso("Lenguaje",4,"Ingenieria industrial")
# print(curso2.nombre)