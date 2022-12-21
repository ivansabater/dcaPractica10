class Usuario: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def mayorEdad(self):
        if (int(self.edad) >= 21):
            return "Eres mayor de edad"
        else:
            return "Eres menor de edad"

anyadirUsuarios = True
listaUsuarios = list()
while(anyadirUsuarios):
    name = input("¿Cual es tu nombre?: ")
    age = input("¿Cual es tu edad?: ")
    listaUsuarios.append(Usuario(name,age))
    i = 1
    for usuario in listaUsuarios:
        print("Usuario " + str(i) + ": \n nombre: " + usuario.getNombre() + ", edad: " + usuario.getEdad() + ", " + usuario.mayorEdad())
        i += 1
    anyadirUsuarios = input("¿Quieres seguir añadiendo usuarios?: ")
