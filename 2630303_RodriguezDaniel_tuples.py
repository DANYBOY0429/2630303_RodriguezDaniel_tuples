#Manejo de Listas, Tuplas y Diccionarios en Python

# Nombre: Daniel Rodriguez Moreno

# Matricula: 2630303

# Grupo: 3

# PRINCIPIOS Y BUENAS PRACTICAS 
"""
- Usar listas cuando necesites agregar o eliminar 
elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar 
(por ejemplo, coordenadas, fechas, configuraciones fijas).
- Usar diccionarios cuando necesites buscar información 
por una clave (por ejemplo, por nombre, id, código).
- Evitar modificar una lista mientras la recorres con un 
for, a menos que sepas exactamente lo que haces.
- Usar nombres de claves descriptivos en los diccionarios 
(por ejemplo, "name", "age", "price").
- Escribir código legible y mensajes claros para el usuario.
"""

# RESUMEN
"""
Las listas en python son consideradas como mutables que 
quiero decir con esto que se pueden ir modificando con el
tiempo y se le pueden asignar nuevos valores.
Por otro lado las tuplas en python son consideradas como 
inmutables que caso contrario que con las listas estas no se
puede  modificar o cambiar el valor con el tiempo.
"""
# PROBLEMS
print('problems'.upper())
print('------------------------------------------')


# Problem 1: Shopping list basics (list operations)

"""
Este programa en Python permite crear una lista de productos 
y sus cantidades, agregar nuevos productos, contar el total 
de elementos y verificar si un producto específico se encuentra 
en la lista mediante un valor booleano (`True` o `False`).
"""

products = ["Laptop", "Mouse", "Teclado", "Monitor"]
quantities = [5, 10, 8, 3]

new_product = input("Ingresa un nuevo producto: ")
new_quantity = int(input("Ingresa la cantidad: "))

products.append(new_product)
quantities.append(new_quantity)

total_elements = len(products)
print("Productos:", products)
print("Cantidades:", quantities)
print("Total de elementos:", total_elements)

product_to_find = input("Producto a buscar: ")
is_in_list = product_to_find in products

print("¿Está en la lista?:", is_in_list)
print('------------------------------------------')

"""
Caso de prueba:

------------------------------------------
"""
#Problem 2: Points and distances with tuples

"""
El programa permite ingresar las coordenadas de dos 
puntos en un plano 2D mediante tuplas. Calcula la distancia 
euclidiana entre ambos puntos y determina el punto medio 
utilizando sus coordenadas.
"""

import math

x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

point_a = (x1, y1)
point_b = (x2, y2)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print("Punto A:", point_a)
print("Punto B:", point_b)
print("Distancia:", distance)
print("Punto medio:", midpoint)

"""
Caso de prueba:
Ingresa x1: 3
Ingresa y1: -2
Ingresa x2: 4
Ingresa y2: 3
Punto A: (3.0, -2.0)
Punto B: (4.0, 3.0)
Distancia: 5.0990195135927845
Punto medio: (3.5, 0.5)
"""

# CONCLUCIONES
"""
El programa permite trabajar con tuplas en Python para 
representar puntos en un plano 2D. Además, utiliza fórmulas 
matemáticas para calcular la distancia entre dos puntos y 
encontrar su punto medio, reforzando el uso de variables, 
operaciones aritméticas y la biblioteca. 
"""

# REFERENCIAS

"""
* Python Software Foundation. Python Documentation: 
Data Structures. [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html?utm_source=chatgpt.com)

* Python Software Foundation. Python Documentation: 
Built-in Functions. [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html?utm_source=chatgpt.com)

* Python Software Foundation. Python Documentation: 
Math Module. [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html?utm_source=chatgpt.com)

* Khan Academy. Distancia entre dos puntos. 
[https://es.khanacademy.org/math/geometry](https://es.khanacademy.org/math/geometry?utm_source=chatgpt.com)

* OpenStax. Precalculus 2e: Analytic Geometry. 
[https://openstax.org/details/books/precalculus-2e](https://openstax.org/details/books/precalculus-2e?utm_source=chatgpt.com)
*
"""