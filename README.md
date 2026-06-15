# Sistema de Gestión de Mascotas

Este repositorio contiene el desarrollo de una actividad práctica diseñada para contrastar la **Programación Tradicional (Estructurada)** con la **Programación Orientada a Objetos (POO)** utilizando Python.

## Información del Estudiante
* **Nombre Completo:** Manuel Damian Ortega Japon
* **Carrera:** Ingeniería en Tecnología de la Información

## Descripción de los Programas
El proyecto resuelve el mismo problema (registrar y mostrar los datos de una mascota) bajo dos paradigmas diferentes:
1. **`programacion_tradicional/`**: Solución basada en funciones que solicita datos dinámicamente por teclado de forma secuencial.
2. **`programacion_poo/`**: Solución dividida en módulos. Define la clase `Mascota` en un archivo y el punto de entrada ejecutable en `main.py`.

## Reflexión: Diferencias entre Programación Tradicional y POO
* **Organización y Modularidad:** La POO nos obliga a separar la plantilla del objeto de la lógica de ejecución, lo que genera un código mucho más limpio y desacoplado que el enfoque tradicional.
* **Abstracción y Reutilización:** En la programación tradicional, manejar múltiples mascotas requiere duplicar variables o gestionar listas complejas de diccionarios. En la POO, basta con instanciar nuevos objetos a partir de la clase base, manteniendo de forma independiente sus atributos y comportamientos, lo que facilita de forma drástica la escalabilidad del sistema.
