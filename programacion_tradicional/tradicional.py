# Damian Ortega tradicional.py
def registrar_mascota():
    print("--- Registro de Mascota (Programación Tradicional) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    edad = input("Ingrese la edad de la mascota: ")
    return {"nombre": nombre, "especie": especie, "edad": edad}

def mostrar_mascota(mascota):
    print("\n--- Información de la Mascota ---")
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")
    print("---------------------------------")

if __name__ == "__main__":
    nueva_mascota = registrar_mascota()
    mostrar_mascota(nueva_mascota)
