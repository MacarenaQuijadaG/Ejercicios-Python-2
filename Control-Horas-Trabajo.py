import datetime
import os

# Sistema de Control de Horas de Trabajo
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horas_trabajadas = 0

    def registrar_hora_entrada(self):
        self.hora_entrada = datetime.datetime.now()
        print(f"Hora de entrada registrada: {self.hora_entrada}")

    def registrar_hora_salida(self):
        self.hora_salida = datetime.datetime.now()
        horas = (self.hora_salida - self.hora_entrada).seconds / 3600
        self.horas_trabajadas += horas
        print(f"Hora de salida registrada: {self.hora_salida}")
        print(f"Horas trabajadas en esta sesión: {horas:.2f} horas")

class SistemaHorasTrabajo:
    def __init__(self):
        self.empleados = {}

    def registrar_empleado(self, nombre):
        if nombre not in self.empleados:
            self.empleados[nombre] = Empleado(nombre)
            print(f"Empleado {nombre} registrado.")
        else:
            print("El empleado ya está registrado.")

    def registrar_entrada(self, nombre):
        if nombre in self.empleados:
            self.empleados[nombre].registrar_hora_entrada()
        else:
            print("Empleado no encontrado.")

    def registrar_salida(self, nombre):
        if nombre in self.empleados:
            self.empleados[nombre].registrar_hora_salida()
        else:
            print("Empleado no encontrado.")

    def generar_reporte(self):
        for nombre, empleado in self.empleados.items():
            print(f"Empleado: {nombre}, Horas acumuladas: {empleado.horas_trabajadas:.2f} horas")


# Gestión de Eventos y Entradas
class Evento:
    def __init__(self, nombre, precio, capacidad):
        self.nombre = nombre
        self.precio = precio
        self.capacidad = capacidad
        self.entradas_vendidas = 0

    def vender_entrada(self, cantidad):
        if self.capacidad - self.entradas_vendidas >= cantidad:
            self.entradas_vendidas += cantidad
            print(f"{cantidad} entradas vendidas para {self.nombre}.")
        else:
            print(f"No hay suficientes entradas disponibles. Solo quedan {self.capacidad - self.entradas_vendidas}.")

class GestionEventos:
    def __init__(self):
        self.eventos = []

    def crear_evento(self, nombre, precio, capacidad):
        evento = Evento(nombre, precio, capacidad)
        self.eventos.append(evento)
        print(f"Evento {nombre} creado con éxito.")

    def vender_entrada(self, nombre_evento, cantidad):
        for evento in self.eventos:
            if evento.nombre == nombre_evento:
                evento.vender_entrada(cantidad)
                return
        print("Evento no encontrado.")


# Simulador de Reparto a Domicilio
import random

class Pedido:
    def __init__(self, restaurante, direccion):
        self.restaurante = restaurante
        self.direccion = direccion

class Repartidor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

class EmpresaReparto:
    def __init__(self):
        self.repartidores = [Repartidor(f"Repartidor {i}") for i in range(1, 6)]

    def asignar_repartidor(self):
        disponibles = [r for r in self.repartidores if r.disponible]
        if disponibles:
            repartidor = random.choice(disponibles)
            repartidor.disponible = False
            return repartidor
        else:
            return None

    def calcular_distancia(self, restaurante, direccion):
        return random.uniform(1, 15)  

    def calcular_tiempo_entrega(self, distancia):
        return distancia * 5  

    def procesar_pedido(self, restaurante, direccion):
        repartidor = self.asignar_repartidor()
        if repartidor:
            distancia = self.calcular_distancia(restaurante, direccion)
            tiempo_estimado = self.calcular_tiempo_entrega(distancia)
            print(f"Pedido asignado a {repartidor.nombre}. Distancia: {distancia:.2f} km, Tiempo estimado: {tiempo_estimado:.2f} minutos.")
        else:
            print("No hay repartidores disponibles en este momento.")



def menu():
    sistema_horas = SistemaHorasTrabajo()
    gestion_eventos = GestionEventos()
    empresa_reparto = EmpresaReparto()

    while True:
        print("\n1. Sistema de Control de Horas de Trabajo")
        print("2. Gestión de Eventos y Entradas")
        print("3. Simulador de Reparto a Domicilio")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Sistema de Control de Horas de Trabajo ---")
                print("1. Registrar empleado")
                print("2. Registrar hora de entrada")
                print("3. Registrar hora de salida")
                print("4. Generar reporte de horas")
                print("5. Volver al menú principal")
                opcion_horas = input("Selecciona una opción: ")

                if opcion_horas == "1":
                    nombre = input("Nombre del empleado: ")
                    sistema_horas.registrar_empleado(nombre)
                elif opcion_horas == "2":
                    nombre = input("Nombre del empleado: ")
                    sistema_horas.registrar_entrada(nombre)
                elif opcion_horas == "3":
                    nombre = input("Nombre del empleado: ")
                    sistema_horas.registrar_salida(nombre)
                elif opcion_horas == "4":
                    sistema_horas.generar_reporte()
                elif opcion_horas == "5":
                    break

        elif opcion == "2":
            while True:
                print("\n--- Gestión de Eventos y Entradas ---")
                print("1. Crear evento")
                print("2. Vender entradas")
                print("3. Volver al menú principal")
                opcion_eventos = input("Selecciona una opción: ")

                if opcion_eventos == "1":
                    nombre = input("Nombre del evento: ")
                    precio = float(input("Precio de la entrada: "))
                    capacidad = int(input("Capacidad del evento: "))
                    gestion_eventos.crear_evento(nombre, precio, capacidad)
                elif opcion_eventos == "2":
                    nombre_evento = input("Nombre del evento: ")
                    cantidad = int(input("Cantidad de entradas a vender: "))
                    gestion_eventos.vender_entrada(nombre_evento, cantidad)
                elif opcion_eventos == "3":
                    break

        elif opcion == "3":
            while True:
                print("\n--- Simulador de Reparto a Domicilio ---")
                print("1. Realizar pedido")
                print("2. Volver al menú principal")
                opcion_reparto = input("Selecciona una opción: ")

                if opcion_reparto == "1":
                    restaurante = input("Nombre del restaurante: ")
                    direccion = input("Dirección de entrega: ")
                    empresa_reparto.procesar_pedido(restaurante, direccion)
                elif opcion_reparto == "2":
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


menu()
