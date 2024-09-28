import random
import math
import datetime

# Simulador de Reparto a Domicilio
class Repartidor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True

    def asignar_pedido(self):
        if not self.disponible:
            raise ValueError(f"El repartidor {self.nombre} no está disponible.")
        self.disponible = False

    def finalizar_pedido(self):
        self.disponible = True

    def __str__(self):
        return f"Repartidor: {self.nombre}, Disponible: {'Sí' if self.disponible else 'No'}"

class Pedido:
    def __init__(self, cliente, restaurante, direccion, distancia):
        self.cliente = cliente
        self.restaurante = restaurante
        self.direccion = direccion
        self.distancia = distancia  # Distancia en kilómetros
        self.repartidor = None

    def asignar_repartidor(self, repartidor):
        self.repartidor = repartidor
        repartidor.asignar_pedido()

    def calcular_tiempo_entrega(self):
        velocidad_promedio = 40  # km/h
        tiempo_est = self.distancia / velocidad_promedio * 60  # En minutos
        return round(tiempo_est, 2)

    def __str__(self):
        return f"Pedido de {self.cliente}, Restaurante: {self.restaurante}, Dirección: {self.direccion}, Distancia: {self.distancia} km, Repartidor: {self.repartidor.nombre}"

class SistemaReparto:
    def __init__(self):
        self.repartidores = []
        self.pedidos = []

    def agregar_repartidor(self, nombre):
        repartidor = Repartidor(nombre)
        self.repartidores.append(repartidor)
        print(f"Repartidor {nombre} agregado.")

    def realizar_pedido(self, cliente, restaurante, direccion, distancia):
        if not self.repartidores:
            print("No hay repartidores disponibles.")
            return
        
        repartidor = self.buscar_repartidor_disponible()
        if repartidor is None:
            print("No hay repartidores disponibles en este momento.")
            return
        
        pedido = Pedido(cliente, restaurante, direccion, distancia)
        pedido.asignar_repartidor(repartidor)
        self.pedidos.append(pedido)
        print(f"Pedido realizado: {pedido}")
        print(f"Tiempo estimado de entrega: {pedido.calcular_tiempo_entrega()} minutos")

    def buscar_repartidor_disponible(self):
        for repartidor in self.repartidores:
            if repartidor.disponible:
                return repartidor
        return None

    def finalizar_pedido(self, cliente):
        for pedido in self.pedidos:
            if pedido.cliente == cliente:
                pedido.repartidor.finalizar_pedido()
                self.pedidos.remove(pedido)
                print(f"Pedido de {cliente} finalizado.")
                return
        print(f"No se encontró un pedido para el cliente {cliente}.")

# Sistema de Reservas para un Gimnasio
class Clase:
    def __init__(self, nombre, cupo_maximo):
        self.nombre = nombre
        self.cupo_maximo = cupo_maximo
        self.reservas = []

    def reservar(self, usuario):
        if len(self.reservas) >= self.cupo_maximo:
            raise ValueError("Cupo lleno para esta clase.")
        self.reservas.append(usuario)
        print(f"{usuario} ha reservado un cupo en {self.nombre}.")

    def cancelar_reserva(self, usuario):
        if usuario in self.reservas:
            self.reservas.remove(usuario)
            print(f"Reserva de {usuario} cancelada.")
        else:
            print(f"{usuario} no tiene una reserva en {self.nombre}.")

    def mostrar_reservas(self):
        return f"Clase: {self.nombre}, Reservas: {', '.join(self.reservas)}, Cupo disponible: {self.cupo_maximo - len(self.reservas)}"

class Gimnasio:
    def __init__(self):
        self.clases = {}

    def agregar_clase(self, nombre, cupo_maximo):
        if nombre in self.clases:
            raise ValueError("Esta clase ya está registrada.")
        clase = Clase(nombre, cupo_maximo)
        self.clases[nombre] = clase
        print(f"Clase {nombre} agregada con cupo máximo de {cupo_maximo}.")

    def reservar_clase(self, nombre, usuario):
        if nombre in self.clases:
            try:
                self.clases[nombre].reservar(usuario)
            except ValueError as e:
                print(e)
        else:
            print(f"La clase {nombre} no está disponible.")

    def cancelar_reserva(self, nombre, usuario):
        if nombre in self.clases:
            self.clases[nombre].cancelar_reserva(usuario)
        else:
            print(f"La clase {nombre} no está disponible.")

    def mostrar_reservas(self, nombre):
        if nombre in self.clases:
            print(self.clases[nombre].mostrar_reservas())
        else:
            print(f"La clase {nombre} no está disponible.")

# Simulador de Mercado de Valores
class Accion:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def fluctuar_precio(self):
        cambio = random.uniform(-0.05, 0.05)
        self.precio += self.precio * cambio
        return round(self.precio, 2)

    def __str__(self):
        return f"Acción: {self.nombre}, Precio actual: ${self.precio}"

class Inversionista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.portafolio = {}

    def comprar_accion(self, accion, cantidad):
        if accion.nombre in self.portafolio:
            self.portafolio[accion.nombre] += cantidad
        else:
            self.portafolio[accion.nombre] = cantidad
        print(f"{self.nombre} ha comprado {cantidad} acciones de {accion.nombre}.")

    def vender_accion(self, accion, cantidad):
        if accion.nombre in self.portafolio and self.portafolio[accion.nombre] >= cantidad:
            self.portafolio[accion.nombre] -= cantidad
            if self.portafolio[accion.nombre] == 0:
                del self.portafolio[accion.nombre]
            print(f"{self.nombre} ha vendido {cantidad} acciones de {accion.nombre}.")
        else:
            print(f"No tienes suficientes acciones de {accion.nombre} para vender.")

    def generar_reporte(self):
        print(f"Portafolio de {self.nombre}:")
        for nombre_accion, cantidad in self.portafolio.items():
            print(f"- {nombre_accion}: {cantidad} acciones")

class Mercado:
    def __init__(self):
        self.acciones = {}

    def agregar_accion(self, nombre, precio_inicial):
        accion = Accion(nombre, precio_inicial)
        self.acciones[nombre] = accion
        print(f"Acción {nombre} agregada con precio inicial de ${precio_inicial}.")

    def fluctuar_precios(self):
        print("Fluctuaciones del mercado:")
        for accion in self.acciones.values():
            nuevo_precio = accion.fluctuar_precio()
            print(f"- {accion.nombre}: ${nuevo_precio}")

    def consultar_accion(self, nombre):
        if nombre in self.acciones:
            print(self.acciones[nombre])
        else:
            print(f"La acción {nombre} no está disponible.")

# Menú principal
def menu():
    sistema_reparto = SistemaReparto()
    gimnasio = Gimnasio()
    mercado = Mercado()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Simulador de Reparto a Domicilio")
        print("2. Sistema de Reservas para un Gimnasio")
        print("3. Simulador de Mercado de Valores")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Simulador de Reparto a Domicilio ---")
                print("1. Agregar repartidor")
                print("2. Realizar pedido")
                print("3. Finalizar pedido")
                print("4. Volver al menú principal")
                opcion_reparto = input("Selecciona una opción: ")

                if opcion_reparto == "1":
                    nombre = input("Nombre del repartidor: ")
                    sistema_reparto.agregar_repartidor(nombre)
                elif opcion_reparto == "2":
                    cliente = input("Nombre del cliente: ")
                    restaurante = input("Nombre del restaurante: ")
                    direccion = input("Dirección del cliente: ")
                    distancia = float(input("Distancia en km desde el restaurante: "))
                    sistema_reparto.realizar_pedido(cliente, restaurante, direccion, distancia)
                elif opcion_reparto == "3":
                    cliente = input("Nombre del cliente para finalizar pedido: ")
                    sistema_reparto.finalizar_pedido(cliente)
                elif opcion_reparto == "4":
                    break

        elif opcion == "2":
            while True:
                print("\n--- Sistema de Reservas para un Gimnasio ---")
                print("1. Agregar clase")
                print("2. Reservar clase")
                print("3. Cancelar reserva")
                print("4. Mostrar reservas")
                print("5. Volver al menú principal")
                opcion_gimnasio = input("Selecciona una opción: ")

                if opcion_gimnasio == "1":
                    nombre = input("Nombre de la clase: ")
                    cupo_maximo = int(input("Cupo máximo: "))
                    gimnasio.agregar_clase(nombre, cupo_maximo)
                elif opcion_gimnasio == "2":
                    nombre_clase = input("Nombre de la clase: ")
                    usuario = input("Nombre del usuario: ")
                    gimnasio.reservar_clase(nombre_clase, usuario)
                elif opcion_gimnasio == "3":
                    nombre_clase = input("Nombre de la clase: ")
                    usuario = input("Nombre del usuario: ")
                    gimnasio.cancelar_reserva(nombre_clase, usuario)
                elif opcion_gimnasio == "4":
                    nombre_clase = input("Nombre de la clase: ")
                    gimnasio.mostrar_reservas(nombre_clase)
                elif opcion_gimnasio == "5":
                    break

        elif opcion == "3":
            while True:
                print("\n--- Simulador de Mercado de Valores ---")
                print("1. Agregar acción")
                print("2. Consultar acción")
                print("3. Fluctuar precios")
                print("4. Volver al menú principal")
                opcion_mercado = input("Selecciona una opción: ")

                if opcion_mercado == "1":
                    nombre = input("Nombre de la acción: ")
                    precio_inicial = float(input("Precio inicial de la acción: "))
                    mercado.agregar_accion(nombre, precio_inicial)
                elif opcion_mercado == "2":
                    nombre = input("Nombre de la acción: ")
                    mercado.consultar_accion(nombre)
                elif opcion_mercado == "3":
                    mercado.fluctuar_precios()
                elif opcion_mercado == "4":
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    menu()
