from decimal import MIN_EMIN
from pickle import TRUE
MIN = 1
MAX = 5

class Menu:
    def __init__(self):
        self.listaUsuario = list()
        self.listaPueblos = list()
    def pintarMenu():
        print("Menú")
        print("1. Usuarios")
        print("2. Pueblos")
        print("3. Centros Escolares")
        print("4. Imprimir por Pantalla")
        print("5. Salida")

    def seleccionarOpcion(self, min, max):
        opcion = input("Elige tu opción: ")
        salida = True
        while(salida):
            try:
                opcion = int(opcion)
                salida = False
            except:
                print("Introduce un número entre el " + str(min) + " y el " + str(max))
                opcion = input("Elige tu opción: ")
        if(opcion < min or opcion > max):
            return opcion
        else:
            return opcion
    def seleccionarMenu(self):
        self.pintarMenu
        opcion = self.seleccionarOpcion(MIN,MAX)
        if opcion == 1:
            self.menuUsuario("Usuario", True)
        elif opcion == 2:
            self.menuUsuario("Pueblo", True)
        elif opcion == 3:
            self.menuUsuario("Centro Escolar", False)

    def seleccionarMenuTipo(self, opcion):
        if opcion == 1:
            usuario = Usuario()
            self.listaUsuario.append(usuario)
            print("Usuario: \n nombre: " + usuario.getNombre() + ", edad: " + str(usuario.getEdad()) + ", " + usuario.mayorEdad())
        elif opcion == 2:
            self.menuUsuario("Pueblo", True)
        elif opcion == 3:
            self.menuUsuario("Centro Escolar", False)
    
    def menuUsuario(self, tipoMenu, plural):
        print("Menú " + tipoMenu)
        print("1. Crear " + tipoMenu)
        print("2. Eliminar " + tipoMenu)
        print("3. Modificar " + tipoMenu)
        if plural == False:
            print("4. Listar " + tipoMenu + "es")
        else:
            print("4. Listar " + tipoMenu + "s")
        print("5. Salida")
        opcion = self.seleccionarOpcion(MIN,MAX)
        self.seleccionarMenuTipo(opcion, tipoMenu)




        


class Usuario: 
    def __init__(self):
        name = input("¿Cual es tu nombre?: ")
        age = input("¿Cual es tu edad?: ")
        age = self.validacionNumero(age)
        self.nombre = name
        self.edad = age
    def validacionNumero(age):
        salida = True
        while(salida):
            try:
                age = int(age)
                salida = False
            except:
                print("Introduce un número")
                age = input("¿Cual es tu edad?: ")
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def mayorEdad(self):
        if (int(self.edad) >= 18):
            return "Eres mayor de edad"
        else:
            return "Eres menor de edad"

class Pueblo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = {
            "Colegio": [],
            "Instituto": [],
            "Universidad": [],
        }
    def getNombre(self):
        return self.nombre
    def getLista(self, centroEstudio):
        return self.lista[centroEstudio]
    def elCentroYaExiste(self, nombre):
        if nombre in self.getLista("Colegio"):
            return True
        elif nombre in self.getLista("Instituto"):
            return True
        elif nombre in self.getLista("Universidad"):
            return True
        else:
            return False
    def anyadirCentro(self, centro):
        if(type(centro) == Colegio):
            self.lista["Colegio"].append(centro)
        elif(type(centro) == Instituto):
            self.lista["Instituto"].append(centro)
        elif(type(centro) == Universidad):
            self.lista["Universidad"].append(centro)

class CentroEscolar:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    def getNombre(self):
        return self.nombre



class Colegio(CentroEscolar):
    def __init__(self, nombre, codigo):
       super().__init__(nombre,codigo)
       self.lista = list()

    def anyadirEstudiante(self, usuario):
        if(usuario.getEdad() >= 6 and usuario.getEdad() < 12):
            self.lista.append(usuario)
        else:
            print("Error: Este estudiante no debe estar en el Colegio")

class Instituto(CentroEscolar):
    def __init__(self, nombre, codigo):
       super().__init__(nombre,codigo)
       self.lista = list()

    def anyadirEstudiante(self, usuario):
        if(usuario.getEdad() >= 12 and usuario.getEdad() < 18):
            self.lista.append(usuario)
        else:
            print("Error: Este estudiante no debe estar en el Instituto")

class Universidad(CentroEscolar):
    def __init__(self, nombre, codigo):
       super().__init__(nombre,codigo)
       self.lista = list()

    def anyadirEstudiante(self, usuario):
        if(usuario.getEdad() >= 21):
            self.lista.append(usuario)
        else:
            print("Error: Este estudiante no debe estar en el Instituto")

anyadirUsuarios = True
anyadirCentro = True
codigo = 0
listaUsuarios = list()
listaPueblos = list()
while(anyadirUsuarios):
    name = input("¿Cual es tu nombre?: ")
    age = input("¿Cual es tu edad?: ")
    salida = True
    while(salida):
        try:
            age = int(age)
            salida = False
        except:
            print("Introduce un número")
            age = input("¿Cual es tu edad?: ")
    listaUsuarios.append(Usuario(name,age))
    i = 1
    for usuario in listaUsuarios:
        print("Usuario " + str(i) + ": \n nombre: " + usuario.getNombre() + ", edad: " + str(usuario.getEdad()) + ", " + usuario.mayorEdad())
        i += 1
    respuesta = input("¿Quieres seguir añadiendo usuarios? (T/F): ")
    while(respuesta.upper() != "T" and respuesta.upper() != "F"):
        respuesta = input("¿Quieres seguir añadiendo usuarios? (T/F): ")
    if (respuesta.upper() == "F"): 
        anyadirUsuarios = False
while(anyadirCentro): 
    nombre = input("¿Cual es el nombre del centro escolar? ")
    nombrePueblo = input("¿En que pueblo está el centro escolar? ")
    estaEnLista = False
    for puebloLista in listaPueblos:
        if puebloLista.getNombre() == nombrePueblo:
            pueblo = puebloLista
            estaEnLista = True
    if estaEnLista == False:
        pueblo = Pueblo(nombrePueblo)
        listaPueblos.append(pueblo)
        estaEnLista = False
    tipoCentroEscolar = input("¿De que tipo de Centro Escolar se trata? \n a. Colegio \n b. Instituto \n c. Universidad \n")
    while(tipoCentroEscolar.upper() != "A" and tipoCentroEscolar.upper() != "B" and tipoCentroEscolar.upper() != "C"):
        tipoCentroEscolar = input("¿De que tipo de Centro Escolar se trata? \n a. Colegio \n b. Instituto \n c. Universidad \n")
    if(tipoCentroEscolar.upper() == "A"):
        centro = Colegio(nombre,codigo)
    elif(tipoCentroEscolar.upper() == "B"):
        centro = Instituto(nombre,codigo)
    elif(tipoCentroEscolar.upper() == "C"):
        centro = Universidad(nombre,codigo)
    pueblo.anyadirCentro(centro)

    respuesta = input("¿Quieres seguir añadiendo centros? (T/F): ")
    while(respuesta.upper() != "T" and respuesta.upper() != "F"):
        respuesta = input("¿Quieres seguir añadiendo centros? (T/F): ")
    if (respuesta.upper() == "F"): 
        anyadirCentro = False
j = 0
i = 0
for pueblos in listaPueblos:
    print("- Pueblo " + str(j) + ": " + pueblos.getNombre())
    k = 0
    x = pueblos.lista.items()
    for i in pueblos.lista.keys(): # Colegio, Instituto, Universidad
        print("-----Estamos en: " + i + "-----")
        for k in range(len(pueblos.lista[i])):
            lista2 = pueblos.lista[i]
            print(lista2[k].getNombre())
    j =j + 1