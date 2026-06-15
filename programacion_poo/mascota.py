# Damian Ortega ingresar los datos de mascotas utilizando programación orientada a objetos (POO)
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        especie_low = self.especie.lower()
        if "perro" in especie_low:
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif "gato" in especie_low:
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido característico.")
