import json

# Simulador de Banco
class CuentaBancaria:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.historial = []

    def depositar(self, monto):
        self.saldo += monto
        self.historial.append(f"Deposito: {monto}")
        print(f"Depósito exitoso. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            self.historial.append(f"Retiro: {monto}")
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")

    def transferir(self, cuenta_destino, monto):
        if monto > self.saldo:
            print("Fondos insuficientes para la transferencia.")
        else:
            self.retirar(monto)
            cuenta_destino.depositar(monto)
            self.historial.append(f"Transferencia a {cuenta_destino.nombre}: {monto}")
            print(f"Transferencia exitosa a {cuenta_destino.nombre}. Saldo actual: {self.saldo}")

    def consultar_saldo(self):
        return self.saldo

    def mostrar_historial(self):
        print("Historial de transacciones:")
        for transaccion in self.historial:
            print(transaccion)


# Sistema de Reservas para Cine
class Cine:
    def __init__(self):
        self.peliculas = {}
        self.asientos = {}

    def agregar_pelicula(self, nombre, horarios, total_asientos):
        self.peliculas[nombre] = horarios
        self.asientos[nombre] = total_asientos
        print(f"Pelicula {nombre} agregada.")

    def reservar_asiento(self, pelicula, horario, asientos_reservados):
        if pelicula not in self.peliculas:
            print("Película no encontrada.")
            return

        if horario not in self.peliculas[pelicula]:
            print("Horario no disponible.")
            return

        if asientos_reservados > self.asientos[pelicula]:
            print("No hay suficientes asientos disponibles.")
        else:
            self.asientos[pelicula] -= asientos_reservados
            print(f"Reserva exitosa para {asientos_reservados} asientos en la película {pelicula} a las {horario}.")
            print(f"Boleto generado para {asientos_reservados} asientos.")


# Sistema de Gestión Escolar
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def asignar_materia(self, materia, nota):
        self.calificaciones[materia] = nota

    def mostrar_calificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for materia, nota in self.calificaciones.items():
            print(f"{materia}: {nota}")


class GestionEscolar:
    def __init__(self):
        self.estudiantes = {}

    def registrar_estudiante(self, nombre):
        self.estudiantes[nombre] = Estudiante(nombre)
        print(f"Estudiante {nombre} registrado.")

    def asignar_calificacion(self, nombre, materia, nota):
        if nombre in self.estudiantes:
            self.estudiantes[nombre].asignar_materia(materia, nota)
            print(f"Calificación asignada: {materia} - {nota} a {nombre}.")
        else:
            print("Estudiante no encontrado.")

    def generar_reporte(self):
        print("Reporte de estudiantes:")
        for estudiante in self.estudiantes.values():
            estudiante.mostrar_calificaciones()


# Función principal
def main():
    banco = {}
    cine = Cine()
    gestion_escolar = GestionEscolar()

    while True:
        print("\nSeleccione una opción:")
        print("1. Simulador de Banco")
        print("2. Sistema de Reservas para Cine")
        print("3. Sistema de Gestión Escolar")
        print("4. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == '1':
            while True:
                print("\nSimulador de Banco:")
                print("1. Crear Cuenta")
                print("2. Hacer Depósito")
                print("3. Hacer Retiro")
                print("4. Transferir Dinero")
                print("5. Consultar Saldo")
                print("6. Mostrar Historial")
                print("7. Volver al menú principal")

                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    nombre = input("Nombre del titular de la cuenta: ")
                    saldo_inicial = float(input("Saldo inicial: "))
                    cuenta = CuentaBancaria(nombre, saldo_inicial)
                    banco[nombre] = cuenta
                    print(f"Cuenta creada para {nombre}.")
                elif sub_opcion == '2':
                    nombre = input("Nombre del titular de la cuenta: ")
                    if nombre in banco:
                        monto = float(input("Monto a depositar: "))
                        banco[nombre].depositar(monto)
                    else:
                        print("Cuenta no encontrada.")
                elif sub_opcion == '3':
                    nombre = input("Nombre del titular de la cuenta: ")
                    if nombre in banco:
                        monto = float(input("Monto a retirar: "))
                        banco[nombre].retirar(monto)
                    else:
                        print("Cuenta no encontrada.")
                elif sub_opcion == '4':
                    nombre_origen = input("Nombre de la cuenta de origen: ")
                    nombre_destino = input("Nombre de la cuenta de destino: ")
                    if nombre_origen in banco and nombre_destino in banco:
                        monto = float(input("Monto a transferir: "))
                        banco[nombre_origen].transferir(banco[nombre_destino], monto)
                    else:
                        print("Una o ambas cuentas no se encontraron.")
                elif sub_opcion == '5':
                    nombre = input("Nombre del titular de la cuenta: ")
                    if nombre in banco:
                        saldo = banco[nombre].consultar_saldo()
                        print(f"Saldo de {nombre}: {saldo}")
                    else:
                        print("Cuenta no encontrada.")
                elif sub_opcion == '6':
                    nombre = input("Nombre del titular de la cuenta: ")
                    if nombre in banco:
                        banco[nombre].mostrar_historial()
                    else:
                        print("Cuenta no encontrada.")
                elif sub_opcion == '7':
                    break

        elif opcion == '2':
            while True:
                print("\nSistema de Reservas para Cine:")
                print("1. Agregar Película")
                print("2. Reservar Asiento")
                print("3. Volver al menú principal")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    nombre = input("Nombre de la película: ")
                    horarios = input("Horarios disponibles (separados por comas): ").split(',')
                    total_asientos = int(input("Total de asientos: "))
                    cine.agregar_pelicula(nombre, [h.strip() for h in horarios], total_asientos)
                elif sub_opcion == '2':
                    pelicula = input("Nombre de la película: ")
                    horario = input("Horario de la película: ")
                    asientos_reservados = int(input("Número de asientos a reservar: "))
                    cine.reservar_asiento(pelicula, horario, asientos_reservados)
                elif sub_opcion == '3':
                    break

        elif opcion == '3':
            while True:
                print("\nSistema de Gestión Escolar:")
                print("1. Registrar Estudiante")
                print("2. Asignar Calificación")
                print("3. Generar Reporte")
                print("4. Volver al menú principal")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    nombre = input("Nombre del estudiante: ")
                    gestion_escolar.registrar_estudiante(nombre)
                elif sub_opcion == '2':
                    nombre = input("Nombre del estudiante: ")
                    materia = input("Materia: ")
                    nota = float(input("Nota: "))
                    gestion_escolar.asignar_calificacion(nombre, materia, nota)
                elif sub_opcion == '3':
                    gestion_escolar.generar_reporte()
                elif sub_opcion == '4':
                    break

        elif opcion == '4':
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
