import csv
import os

# Clase para gestionar contactos
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class GestionContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")

    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]
        print("Contacto eliminado.")

    def buscar_contacto(self, nombre=None, telefono=None, email=None):
        for contacto in self.contactos:
            if (nombre and contacto.nombre == nombre) or \
               (telefono and contacto.telefono == telefono) or \
               (email and contacto.email == email):
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print("Contacto no encontrado.")

    def importar_contactos(self, archivo):
        if os.path.exists(archivo):
            with open(archivo, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.agregar_contacto(row[0], row[1], row[2])
            print("Contactos importados.")
        else:
            print("El archivo no existe.")

    def exportar_contactos(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for contacto in self.contactos:
                writer.writerow([contacto.nombre, contacto.telefono, contacto.email])
        print("Contactos exportados.")


# Clase para simular ventas de ropa
class Producto:
    def __init__(self, categoria, nombre, precio):
        self.categoria = categoria
        self.nombre = nombre
        self.precio = precio

class SimuladorVentas:
    def __init__(self):
        self.productos = [
            Producto("Camisas", "Camisa Azul", 25),
            Producto("Pantalones", "Pantalón Negro", 40),
            Producto("Zapatos", "Zapatos de Cuero", 60)
        ]
        self.carrito = []

    def buscar_producto(self, categoria):
        resultados = list(filter(lambda p: p.categoria == categoria, self.productos))
        if resultados:
            for producto in resultados:
                print(f"{producto.nombre} - ${producto.precio}")
        else:
            print("No hay productos en esta categoría.")

    def agregar_al_carrito(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.carrito.append(producto)
                print(f"{producto.nombre} agregado al carrito.")
                return
        print("Producto no encontrado.")

    def realizar_pago(self):
        total = sum([p.precio for p in self.carrito])
        if total > 100:
            descuento = total * 0.1
            total -= descuento
            print(f"Se aplicó un descuento de ${descuento:.2f}.")
        print(f"Total a pagar: ${total:.2f}")
        self.carrito = []

# Clase para gestionar inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        print("Producto registrado.")

    def actualizar_cantidad(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            print("Cantidad actualizada.")
        else:
            print("Producto no encontrado.")

    def consultar_stock(self, nombre):
        if nombre in self.productos:
            print(f"El stock de {nombre} es: {self.productos[nombre]}")
        else:
            print("Producto no encontrado.")

    def generar_reporte_bajo_stock(self):
        print("Productos con bajo stock:")
        for nombre, cantidad in self.productos.items():
            if cantidad < 10:
                print(f"{nombre}: {cantidad} unidades")


# Menú principal
def menu():
    while True:
        print("\n1. Sistema de Gestión de Contactos")
        print("2. Simulador de Ventas de Ropa en Línea")
        print("3. Sistema de Control de Inventario en un Almacén")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            gestion_contactos = GestionContactos()
            while True:
                print("\n--- Gestión de Contactos ---")
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
                    nombre = input("Nombre: ")
                    gestion_contactos.buscar_contacto(nombre=nombre)
                elif opcion_contactos == "4":
                    archivo = input("Ruta del archivo CSV: ")
                    gestion_contactos.importar_contactos(archivo)
                elif opcion_contactos == "5":
                    archivo = input("Ruta del archivo CSV para exportar: ")
                    gestion_contactos.exportar_contactos(archivo)
                elif opcion_contactos == "6":
                    break

        elif opcion == "2":
            simulador = SimuladorVentas()
            while True:
                print("\n--- Simulador de Ventas de Ropa en Línea ---")
                print("1. Buscar producto por categoría")
                print("2. Agregar producto al carrito")
                print("3. Realizar pago")
                print("4. Volver al menú principal")
                opcion_ventas = input("Selecciona una opción: ")

                if opcion_ventas == "1":
                    categoria = input("Categoría (Camisas, Pantalones, Zapatos): ")
                    simulador.buscar_producto(categoria)
                elif opcion_ventas == "2":
                    nombre = input("Nombre del producto a agregar: ")
                    simulador.agregar_al_carrito(nombre)
                elif opcion_ventas == "3":
                    simulador.realizar_pago()
                elif opcion_ventas == "4":
                    break

        elif opcion == "3":
            inventario = Inventario()
            while True:
                print("\n--- Sistema de Control de Inventario ---")
                print("1. Registrar producto")
                print("2. Actualizar cantidad de producto")
                print("3. Consultar stock")
                print("4. Generar reporte de bajo stock")
                print("5. Volver al menú principal")
                opcion_inventario = input("Selecciona una opción: ")

                if opcion_inventario == "1":
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("Cantidad: "))
                    inventario.registrar_producto(nombre, cantidad)
                elif opcion_inventario == "2":
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("Nueva cantidad: "))
                    inventario.actualizar_cantidad(nombre, cantidad)
                elif opcion_inventario == "3":
                    nombre = input("Nombre del producto: ")
                    inventario.consultar_stock(nombre)
                elif opcion_inventario == "4":
                    inventario.generar_reporte_bajo_stock()
                elif opcion_inventario == "5":
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()
