# Definición clase Fruta
class Fruta:
    def __init__(self, id, nombre, precio_unitario, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
    
    # calcular el costo total 
    def costo_total(self):
        return self.precio_unitario * self.cantidad

# Función recibir fruta
def recibir_fruta_por_teclado():
    id = int(input("Ingrese el ID de la fruta: "))
    nombre = input("Ingrese el nombre de la fruta: ")
    precio_unitario = float(input("Ingrese el precio unitario de la fruta: "))
    cantidad = int(input("Ingrese la cantidad de la fruta: "))
    return Fruta(id, nombre, precio_unitario, cantidad)

# Función  costo total del salpicon.
def mostrar_costo_total(frutas):
    costo_total = sum(fruta.costo_total() for fruta in frutas)
    print(f"El costo total del salpicón es: {costo_total}")

# Función ordenar de mayor a menor costo
def mostrar_frutas_ordenadas_por_costo(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x.costo_total(), reverse=True)
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta.id}, Nombre: {fruta.nombre}, Precio unitario: {fruta.precio_unitario}, Cantidad: {fruta.cantidad}")

# Función mostrar fruta más barata
def mostrar_fruta_mas_barata(frutas):
    fruta_mas_barata = min(frutas, key=lambda x: x.precio_unitario)
    print(f"La fruta más barata es: {fruta_mas_barata.nombre}, Precio unitario: {fruta_mas_barata.precio_unitario}")

# Función principal 
def main():
    # Solicitar al usuario la cantidad de frutas
    N = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    
    # Recibir las frutas por teclado
    frutas = []
    for i in range(N):
        print(f"\nFruta {i+1}:")
        fruta = recibir_fruta_por_teclado()
        frutas.append(fruta)
    
    # Mostrar el costo total del salpicón
    mostrar_costo_total(frutas)
    
    # Mostrar todas las frutas ordenadas de mayor a menor costo
    mostrar_frutas_ordenadas_por_costo(frutas)
    
    # Mostrar la fruta más barata
    mostrar_fruta_mas_barata(frutas)

# Llamada a la función principal del programa
if __name__ == "__main__":
    main()
