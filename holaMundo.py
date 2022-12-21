class Usuario: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad

anyadirUsuarios = True
while(anyadirUsuarios):
    name = input("¿Cual es tu nombre?: ")
    print("Hola Mundo " + name)
    age = input("¿Cual es tu edad?: ")
    if (int(age) >= 21):
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    usuario = Usuario(name,age)
    print(usuario.getNombre())
    print(usuario.getEdad())
    anyadirUsuarios = input("¿Quieres seguir añadiendo usuarios?: ")
