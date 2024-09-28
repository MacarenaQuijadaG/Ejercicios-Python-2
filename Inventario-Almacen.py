import datetime
import csv

# Sistema de Control de Inventario en un Almacén
class Producto:
    def __init__(self, nombre, cantidad, stock_minimo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.stock_minimo = stock_minimo

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad
        if self.cantidad < 0:
            self.cantidad = 0
            raise ValueError("No puede tener un stock negativo.")

    def es_stock_bajo(self):
        return self.cantidad < self.stock_minimo

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Stock mínimo: {self.stock_minimo}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, cantidad, stock_minimo):
        if nombre in self.productos:
            raise ValueError("El producto ya está registrado.")
        producto = Producto(nombre, cantidad, stock_minimo)
        self.productos[nombre] = producto
        print(f"Producto registrado: {producto}")

    def actualizar_producto(self, nombre, cantidad):
        if nombre not in self.productos:
            raise ValueError("Producto no encontrado.")
        producto = self.productos[nombre]
        producto.actualizar_cantidad(cantidad)
        print(f"Cantidad actualizada: {producto}")

    def consultar_stock(self, nombre):
        if nombre in self.productos:
            print(self.productos[nombre])
        else:
            print(f"Producto {nombre} no encontrado.")

    def reporte_stock_bajo(self):
        print("Productos con stock bajo:")
        for producto in self.productos.values():
            if producto.es_stock_bajo():
                print(producto)

# Sistema de Control de Horas de Trabajo
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.entradas = []
        self.salidas = []

    def registrar_entrada(self):
        hora_entrada = datetime.datetime.now()
        self.entradas.append(hora_entrada)
        print(f"Hora de entrada registrada para {self.nombre}: {hora_entrada}")

    def registrar_salida(self):
        if not self.entradas:
            raise ValueError("No hay una hora de entrada registrada.")
        hora_salida = datetime.datetime.now()
        self.salidas.append(hora_salida)
        print(f"Hora de salida registrada para {self.nombre}: {hora_salida}")

    def calcular_horas_trabajadas(self):
        total_horas = sum((salida - entrada).total_seconds() for entrada, salida in zip(self.entradas, self.salidas)) / 3600
        return round(total_horas, 2)

    def generar_reporte(self):
        horas_totales = self.calcular_horas_trabajadas()
        print(f"Empleado: {self.nombre}, Horas trabajadas: {horas_totales} horas")

class ControlHoras:
    def __init__(self):
        self.empleados = {}

    def registrar_empleado(self, nombre):
        if nombre in self.empleados:
            raise ValueError("El empleado ya está registrado.")
        empleado = Empleado(nombre)
        self.empleados[nombre] = empleado
        print(f"Empleado {nombre} registrado.")

    def registrar_entrada(self, nombre):
        if nombre in self.empleados:
            self.empleados[nombre].registrar_entrada()
        else:
            print(f"Empleado {nombre} no encontrado.")

    def registrar_salida(self, nombre):
        if nombre in self.empleados:
            self.empleados[nombre].registrar_salida()
        else:
            print(f"Empleado {nombre} no encontrado.")

    def generar_reporte_empleado(self, nombre):
        if nombre in self.empleados:
            self.empleados[nombre].generar_reporte()
        else:
            print(f"Empleado {nombre} no encontrado.")

# Gestión de Eventos y Entradas
class Evento:
    def __init__(self, nombre, precio, entradas_disponibles):
        self.nombre = nombre
        self.precio = precio
        self.entradas_disponibles = entradas_disponibles

    def vender_entrada(self, cantidad):
        if cantidad > self.entradas_disponibles:
            raise ValueError("No hay suficientes entradas disponibles.")
        self.entradas_disponibles -= cantidad
        print(f"Se vendieron {cantidad} entradas para {self.nombre}")

    def __str__(self):
        return f"Evento: {self.nombre}, Precio: ${self.precio}, Entradas disponibles: {self.entradas_disponibles}"

class GestionEventos:
    def __init__(self):
        self.eventos = {}

    def crear_evento(self, nombre, precio, entradas_disponibles):
        if nombre in self.eventos:
            raise ValueError("El evento ya está registrado.")
        evento = Evento(nombre, precio, entradas_disponibles)
        self.eventos[nombre] = evento
        print(f"Evento registrado: {evento}")

    def vender_entradas(self, nombre, cantidad):
        if nombre in self.eventos:
            self.eventos[nombre].vender_entrada(cantidad)
        else:
            print(f"Evento {nombre} no encontrado.")

    def consultar_evento(self, nombre):
        if nombre in self.eventos:
            print(self.eventos[nombre])
        else:
            print(f"Evento {nombre} no encontrado.")

# Menú principal
def menu():
    inventario = Inventario()
    control_horas = ControlHoras()
    gestion_eventos = GestionEventos()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Sistema de Control de Inventario")
        print("2. Sistema de Control de Horas de Trabajo")
        print("3. Gestión de Eventos y Entradas")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Sistema de Control de Inventario ---")
                print("1. Registrar producto")
                print("2. Actualizar cantidad de producto")
                print("3. Consultar stock de un producto")
                print("4. Generar reporte de stock bajo")
                print("5. Volver al menú principal")
                opcion_inventario = input("Selecciona una opción: ")

                if opcion_inventario == "1":
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("Cantidad: "))
                    stock_minimo = int(input("Stock mínimo: "))
                    try:
                        inventario.registrar_producto(nombre, cantidad, stock_minimo)
                    except ValueError as e:
                        print(e)
                elif opcion_inventario == "2":
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("Cantidad a actualizar (+/-): "))
                    try:
                        inventario.actualizar_producto(nombre, cantidad)
                    except ValueError as e:
                        print(e)
                elif opcion_inventario == "3":
                    nombre = input("Nombre del producto: ")
                    inventario.consultar_stock(nombre)
                elif opcion_inventario == "4":
                    inventario.reporte_stock_bajo()
                elif opcion_inventario == "5":
                    break

        elif opcion == "2":
            while True:
                print("\n--- Sistema de Control de Horas de Trabajo ---")
                print("1. Registrar empleado")
                print("2. Registrar entrada")
                print("3. Registrar salida")
                print("4. Generar reporte de horas trabajadas")
                print("5. Volver al menú principal")
                opcion_horas = input("Selecciona una opción: ")

                if opcion_horas == "1":
                    nombre = input("Nombre del empleado: ")
                    try:
                        control_horas.registrar_empleado(nombre)
                    except ValueError as e:
                        print(e)
                elif opcion_horas == "2":
                    nombre = input("Nombre del empleado: ")
                    control_horas.registrar_entrada(nombre)
                elif opcion_horas == "3":
                    nombre = input("Nombre del empleado: ")
                    control_horas.registrar_salida(nombre)
                elif opcion_horas == "4":
                    nombre = input("Nombre del empleado: ")
                    control_horas.generar_reporte_empleado(nombre)
                elif opcion_horas == "5":
                    break

        elif opcion == "3":
            while True:
                print("\n--- Gestión de Eventos y Entradas ---")
                print("1. Crear evento")
                print("2. Vender entradas")
                print("3. Consultar evento")
                print("4. Volver al menú principal")
                opcion_eventos = input("Selecciona una opción: ")

                if opcion_eventos == "1":
                    nombre = input("Nombre del evento: ")
                    precio = float(input("Precio de la entrada: "))
                    entradas_disponibles = int(input("Entradas disponibles: "))
                    try:
                        gestion_eventos.crear_evento(nombre, precio, entradas_disponibles)
                    except ValueError as e:
                        print(e)
                elif opcion_eventos == "2":
                    nombre = input("Nombre del evento: ")
                    cantidad = int(input("Cantidad de entradas a vender: "))
                    try:
                        gestion_eventos.vender_entradas(nombre, cantidad)
                    except ValueError as e:
                        print(e)
                elif opcion_eventos == "3":
                    nombre = input("Nombre del evento: ")
                    gestion_eventos.consultar_evento(nombre)
                elif opcion_eventos == "4":
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    menu()
