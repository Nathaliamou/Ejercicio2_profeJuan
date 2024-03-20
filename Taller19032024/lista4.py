import random
import subprocess

# Función para calcular el promedio de una lista de números
def calcular_promedio(lista):
    total = sum(lista)
    cantidad_elementos = len(lista)
    promedio = total / cantidad_elementos
    return promedio

# Lista de números para calcular el promedio
numeros = [10, 20, 30, 40, 50]
resultado_promedio = calcular_promedio(numeros)

# Función para mostrar todos los productos en la bodega
def mostrar_productos_en_bodega(bodega):
    print("Productos en bodega:")
    for producto, cantidad in bodega.items():
        print(f"{producto}: {cantidad}")

# Función para buscar y mostrar información de un producto específico por nombre
def buscar_producto_por_nombre(bodega_detalles, nombre_producto):
    if nombre_producto in bodega_detalles:
        producto_info = bodega_detalles[nombre_producto]
        print("Información del producto:")
        for key, value in producto_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(f"El producto '{nombre_producto}' no se encuentra en la bodega.")

# Función para modificar el número de unidades compradas de un producto
def modificar_unidades_compradas(bodega, nombre_producto, nuevas_unidades):
    if nombre_producto in bodega:
        bodega[nombre_producto]["cantidad"] = nuevas_unidades
        print(f"El número de unidades compradas de '{nombre_producto}' ha sido modificado a {nuevas_unidades}.")
    else:
        print(f"Error: El producto '{nombre_producto}' no se encuentra en la bodega.")


# Función para eliminar un producto del inventario
def eliminar_producto(bodega, nombre_producto):
    if nombre_producto in bodega:
        confirmacion = input(f"¿Estás seguro de que deseas eliminar '{nombre_producto}' del inventario? (s/n): ")
        if confirmacion.lower() == 's':
            del bodega[nombre_producto]
            print(f"El producto '{nombre_producto}' ha sido eliminado del inventario.")
        else:
            print("La operación ha sido cancelada.")
    else:
        print(f"Error: El producto '{nombre_producto}' no se encuentra en el inventario.")

# Definición de la bodega con productos y cantidades
bodega = {
    "Manzanas": {"cantidad": 100, "precio_unitario": 2.5},
    "Plátanos": {"cantidad": 50, "precio_unitario": 1.75},
    "Naranjas": {"cantidad": 75, "precio_unitario": 3.0},
    "Peras": {"cantidad": 30, "precio_unitario": 2.0}
}
# Estructura de datos para la información detallada de productos
bodega_detalles = {
    "Manzanas": {"Id": 1, "Precio": 2.5, "Descripción": "Manzanas frescas de temporada."},
    "Plátanos": {"Id": 2, "Precio": 1.75, "Descripción": "Plátanos maduros de alta calidad."},
    "Naranjas": {"Id": 3, "Precio": 3.0, "Descripción": "Naranjas jugosas y llenas de sabor."},
    "Peras": {"Id": 4, "Precio": 2.0, "Descripción": "Peras dulces y refrescantes."}
}

# Menú principal
while True:
    print("\n*** Menú Principal ***")
    print("1. Mostrar promedio de una lista de números")
    print("2. Mostrar productos en bodega")
    print("3. Buscar información de un producto")
    print("4. Modificar unidades compradas de un producto")
    print("5. Eliminar un producto del inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("El promedio de la lista es:", resultado_promedio)
    elif opcion == "2":
        mostrar_productos_en_bodega(bodega)
    elif opcion == "3":
        nombre_producto = input("Ingrese el nombre del producto: ")
        buscar_producto_por_nombre(bodega_detalles, nombre_producto)
    elif opcion == "4":
        nombre_producto = input("Ingrese el nombre del producto: ")
        nuevas_unidades = int(input("Ingrese la nueva cantidad de unidades compradas: "))
        modificar_unidades_compradas(bodega, nombre_producto, nuevas_unidades)
    elif opcion == "5":
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(bodega, nombre_producto)
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        # Llamada a subprocess.run() para abrir la consola
subprocess.run(['cmd'])
