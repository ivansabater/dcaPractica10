class Usuario: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        
name = input("¿Cual es tu nombre?: ")
print("Hola Mundo " + name)
age = input("¿Cual es tu edad?: ")
if (int(age) >= 18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
usuario = Usuario(name,age)
print(usuario)
