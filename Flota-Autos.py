import csv
import random

# Sistema de Gestión de Flota de Autos
class Auto:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.estado = "disponible"  # disponible, alquilado, mantenimiento

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible", "alquilado", "mantenimiento"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado inválido")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.tipo}) - Estado: {self.estado}"

class GestionFlota:
    def __init__(self):
        self.autos = []

    def registrar_auto(self, marca, modelo, tipo):
        auto = Auto(marca, modelo, tipo)
        self.autos.append(auto)
        print(f"Auto registrado: {auto}")

    def cambiar_estado_auto(self, indice, nuevo_estado):
        try:
            self.autos[indice].cambiar_estado(nuevo_estado)
            print(f"Estado actualizado: {self.autos[indice]}")
        except IndexError:
            print("Auto no encontrado.")
        except ValueError as e:
            print(e)

    def consultar_disponibilidad(self):
        disponibles = [auto for auto in self.autos if auto.estado == "disponible"]
        if disponibles:
            for auto in disponibles:
                print(auto)
        else:
            print("No hay autos disponibles.")

# Sistema de Gestión de Contactos
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class GestionContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print(f"Contacto agregado: {contacto}")

    def eliminar_contacto(self, nombre):
        self.contactos = [contacto for contacto in self.contactos if contacto.nombre != nombre]
        print(f"Contacto '{nombre}' eliminado.")

    def buscar_contacto(self, query):
        resultados = [contacto for contacto in self.contactos if query in contacto.nombre or query in contacto.telefono or query in contacto.email]
        if resultados:
            for contacto in resultados:
                print(contacto)
        else:
            print(f"No se encontraron contactos con el criterio: {query}")

    def importar_contactos(self, archivo_csv):
        try:
            with open(archivo_csv, mode='r') as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    nombre, telefono, email = fila
                    self.agregar_contacto(nombre, telefono, email)
            print("Contactos importados correctamente.")
        except FileNotFoundError:
            print(f"Archivo {archivo_csv} no encontrado.")

    def exportar_contactos(self, archivo_csv):
        try:
            with open(archivo_csv, mode='w', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                for contacto in self.contactos:
                    escritor_csv.writerow([contacto.nombre, contacto.telefono, contacto.email])
            print("Contactos exportados correctamente.")
        except Exception as e:
            print(f"Error al exportar contactos: {e}")

# Simulador de Ventas de Ropa en Línea
class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio:.2f}"

class TiendaRopa:
    def __init__(self):
        self.productos = [
            Producto("Camisa Azul", "Camisas", 25.99),
            Producto("Pantalón Negro", "Pantalones", 35.50),
            Producto("Zapatos Deportivos", "Zapatos", 55.00),
            Producto("Camisa Blanca", "Camisas", 22.00),
            Producto("Zapatos de Cuero", "Zapatos", 70.00),
        ]
        self.carrito = []

    def buscar_productos(self, categoria):
        resultados = list(filter(lambda producto: producto.categoria == categoria, self.productos))
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print(f"No hay productos disponibles en la categoría: {categoria}")

    def agregar_al_carrito(self, nombre_producto):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            self.carrito.append(producto)
            print(f"{producto.nombre} agregado al carrito.")
        else:
            print(f"Producto {nombre_producto} no encontrado.")

    def calcular_total(self):
        total = sum(producto.precio for producto in self.carrito)
        if total > 100:
            descuento = total * 0.10
            total -= descuento
            print(f"Se ha aplicado un descuento del 10%.")
        print(f"Total a pagar: ${total:.2f}")
        self.carrito = []  

# Menú principal
def menu():
    gestion_flota = GestionFlota()
    gestion_contactos = GestionContactos()
    tienda_ropa = TiendaRopa()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Flota de Autos")
        print("2. Sistema de Gestión de Contactos")
        print("3. Simulador de Ventas de Ropa en Línea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Gestión de Flota de Autos ---")
                print("1. Registrar auto")
                print("2. Cambiar estado de auto")
                print("3. Consultar disponibilidad")
                print("4. Volver al menú principal")
                opcion_flota = input("Selecciona una opción: ")

                if opcion_flota == "1":
                    marca = input("Marca del auto: ")
                    modelo = input("Modelo del auto: ")
                    tipo = input("Tipo de auto (SUV, Sedán, etc.): ")
                    gestion_flota.registrar_auto(marca, modelo, tipo)
                elif opcion_flota == "2":
                    gestion_flota.consultar_disponibilidad()
                    indice_auto = int(input("Selecciona el número del auto: ")) - 1
                    nuevo_estado = input("Nuevo estado (disponible, alquilado, mantenimiento): ")
                    gestion_flota.cambiar_estado_auto(indice_auto, nuevo_estado)
                elif opcion_flota == "3":
                    gestion_flota.consultar_disponibilidad()
                elif opcion_flota == "4":
                    break

        elif opcion == "2":
            while True:
                print("\n--- Sistema de Gestión de Contactos ---")
                print("1. Agregar contacto")
                print("2. Eliminar contacto")
                print("3. Buscar contacto")
                print("4. Importar contactos desde CSV")
                print("5. Exportar contactos a CSV")
                print("6. Volver al menú principal")
                opcion_contactos = input("Selecciona una opción: ")

                if opcion_contactos == "1":
                    nombre = input("Nombre: ")
                    telefono = input("Teléfono: ")
                    email = input("Email: ")
                    gestion_contactos.agregar_contacto(nombre, telefono, email)
                elif opcion_contactos == "2":
                    nombre = input("Nombre del contacto a eliminar: ")
                    gestion_contactos.eliminar_contacto(nombre)
                elif opcion_contactos == "3":
                    query = input("Buscar por nombre, teléfono o email: ")
                    gestion_contactos.buscar_contacto(query)
                elif opcion_contactos == "4":
                    archivo = input("Nombre del archivo CSV para importar: ")
                    gestion_contactos.importar_contactos(archivo)
                elif opcion_contactos == "5":
                    archivo = input("Nombre del archivo CSV para exportar: ")
                    gestion_contactos.exportar_contactos(archivo)
                elif opcion_contactos == "6":
                    break

        elif opcion == "3":
            while True:
                print("\n--- Simulador de Ventas de Ropa en Línea ---")
                print("1. Buscar productos por categoría")
                print("2. Agregar producto al carrito")
                print("3. Pagar")
                print("4. Volver al menú principal")
                opcion_ropa = input("Selecciona una opción: ")

                if opcion_ropa == "1":
                    categoria = input("Categoría (Camisas, Pantalones, Zapatos): ")
                    tienda_ropa.buscar_productos(categoria)
                elif opcion_ropa == "2":
                    nombre_producto = input("Nombre del producto: ")
                    tienda_ropa.agregar_al_carrito(nombre_producto)
                elif opcion_ropa == "3":
                    tienda_ropa.calcular_total()
                elif opcion_ropa == "4":
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    menu()
