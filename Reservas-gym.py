import random
import os

# Sistema de Reservas para un Gimnasio
class ClaseGimnasio:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.cupo = cupo
        self.reservados = 0

    def reservar(self):
        if self.cupo - self.reservados > 0:
            self.reservados += 1
            print(f"Reserva exitosa para {self.nombre}. Cupos restantes: {self.cupo - self.reservados}")
        else:
            print(f"No quedan cupos disponibles para {self.nombre}.")

    def cancelar_reserva(self):
        if self.reservados > 0:
            self.reservados -= 1
            print(f"Reserva cancelada para {self.nombre}. Cupos restantes: {self.cupo - self.reservados}")
        else:
            print(f"No hay reservas para cancelar en {self.nombre}.")

class SistemaGimnasio:
    def __init__(self):
        self.clases = [ClaseGimnasio("Yoga", 10), ClaseGimnasio("Spinning", 8), ClaseGimnasio("CrossFit", 12)]

    def mostrar_clases(self):
        for i, clase in enumerate(self.clases):
            print(f"{i+1}. {clase.nombre} - Cupos disponibles: {clase.cupo - clase.reservados}")

    def reservar_clase(self, indice):
        if 0 <= indice < len(self.clases):
            self.clases[indice].reservar()
        else:
            print("Clase no válida.")

    def cancelar_reserva(self, indice):
        if 0 <= indice < len(self.clases):
            self.clases[indice].cancelar_reserva()
        else:
            print("Clase no válida.")


# Simulador de Mercado de Valores
class Accion:
    def __init__(self, nombre, precio_inicial):
        self.nombre = nombre
        self.precio = precio_inicial

    def fluctuar_precio(self):
        self.precio += random.uniform(-5, 5)

class UsuarioBolsa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.portafolio = {}
        self.balance = 10000

    def comprar_accion(self, accion, cantidad):
        costo = accion.precio * cantidad
        if costo <= self.balance:
            self.balance -= costo
            if accion.nombre in self.portafolio:
                self.portafolio[accion.nombre]["cantidad"] += cantidad
            else:
                self.portafolio[accion.nombre] = {"cantidad": cantidad, "precio_compra": accion.precio}
            print(f"Has comprado {cantidad} acciones de {accion.nombre}. Nuevo balance: {self.balance:.2f}")
        else:
            print("Fondos insuficientes.")

    def vender_accion(self, accion, cantidad):
        if accion.nombre in self.portafolio and self.portafolio[accion.nombre]["cantidad"] >= cantidad:
            ganancia = accion.precio * cantidad
            self.portafolio[accion.nombre]["cantidad"] -= cantidad
            self.balance += ganancia
            print(f"Has vendido {cantidad} acciones de {accion.nombre}. Nuevo balance: {self.balance:.2f}")
        else:
            print("No tienes suficientes acciones para vender.")

    def mostrar_portafolio(self):
        for nombre, datos in self.portafolio.items():
            print(f"Acción: {nombre}, Cantidad: {datos['cantidad']}, Precio compra: {datos['precio_compra']:.2f}")


# Sistema de Gestión de Restaurante
class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.pedidos = []

    def agregar_pedido(self, plato):
        self.pedidos.append(plato)
        print(f"Pedido de {plato.nombre} agregado a la mesa {self.numero}.")

    def mostrar_cuenta(self):
        total = sum(plato.precio for plato in self.pedidos)
        impuestos = total * 0.19
        total_con_impuestos = total + impuestos
        print(f"Cuenta para la mesa {self.numero}:")
        for plato in self.pedidos:
            print(f"- {plato.nombre}: ${plato.precio:.2f}")
        print(f"Subtotal: ${total:.2f}")
        print(f"Impuestos (19%): ${impuestos:.2f}")
        print(f"Total: ${total_con_impuestos:.2f}")


# Menú principal
def menu():
    sistema_gimnasio = SistemaGimnasio()
    mercado_valores = [Accion("Apple", 150), Accion("Google", 2800), Accion("Tesla", 750)]
    usuario_bolsa = UsuarioBolsa("Inversionista")
    mesas_restaurante = [Mesa(1), Mesa(2), Mesa(3)]
    platos_restaurante = [Plato("Hamburguesa", 8.50), Plato("Pizza", 12.00), Plato("Ensalada", 7.00)]

    while True:
        print("\n1. Sistema de Reservas para un Gimnasio")
        print("2. Simulador de Mercado de Valores")
        print("3. Sistema de Gestión de Restaurante")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Sistema de Reservas para un Gimnasio ---")
                sistema_gimnasio.mostrar_clases()
                print("1. Reservar clase")
                print("2. Cancelar reserva")
                print("3. Volver al menú principal")
                opcion_gimnasio = input("Selecciona una opción: ")

                if opcion_gimnasio == "1":
                    indice_clase = int(input("Selecciona el número de la clase a reservar: ")) - 1
                    sistema_gimnasio.reservar_clase(indice_clase)
                elif opcion_gimnasio == "2":
                    indice_clase = int(input("Selecciona el número de la clase a cancelar: ")) - 1
                    sistema_gimnasio.cancelar_reserva(indice_clase)
                elif opcion_gimnasio == "3":
                    break

        elif opcion == "2":
            while True:
                print("\n--- Simulador de Mercado de Valores ---")
                for i, accion in enumerate(mercado_valores):
                    accion.fluctuar_precio()
                    print(f"{i+1}. {accion.nombre}: ${accion.precio:.2f}")
                print("1. Comprar acción")
                print("2. Vender acción")
                print("3. Mostrar portafolio")
                print("4. Volver al menú principal")
                opcion_bolsa = input("Selecciona una opción: ")

                if opcion_bolsa == "1":
                    indice_accion = int(input("Selecciona la acción que quieres comprar: ")) - 1
                    cantidad = int(input("Cantidad de acciones: "))
                    usuario_bolsa.comprar_accion(mercado_valores[indice_accion], cantidad)
                elif opcion_bolsa == "2":
                    indice_accion = int(input("Selecciona la acción que quieres vender: ")) - 1
                    cantidad = int(input("Cantidad de acciones: "))
                    usuario_bolsa.vender_accion(mercado_valores[indice_accion], cantidad)
                elif opcion_bolsa == "3":
                    usuario_bolsa.mostrar_portafolio()
                elif opcion_bolsa == "4":
                    break

        elif opcion == "3":
            while True:
                print("\n--- Sistema de Gestión de Restaurante ---")
                for i, mesa in enumerate(mesas_restaurante):
                    print(f"{i+1}. Mesa {mesa.numero}")
                indice_mesa = int(input("Selecciona la mesa: ")) - 1
                mesa = mesas_restaurante[indice_mesa]

                print("1. Agregar pedido")
                print("2. Mostrar cuenta")
                print("3. Volver al menú principal")
                opcion_restaurante = input("Selecciona una opción: ")

                if opcion_restaurante == "1":
                    for i, plato in enumerate(platos_restaurante):
                        print(f"{i+1}. {plato.nombre}: ${plato.precio:.2f}")
                    indice_plato = int(input("Selecciona el plato: ")) - 1
                    mesa.agregar_pedido(platos_restaurante[indice_plato])
                elif opcion_restaurante == "2":
                    mesa.mostrar_cuenta()
                elif opcion_restaurante == "3":
                    break

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


menu()
