import datetime
import json

# Clase para gestión de citas médicas
class CitaMedica:
    def __init__(self):
        self.pacientes = {}
        self.citas = []

    def registrar_paciente(self, nombre, dni):
        self.pacientes[dni] = nombre
        print(f"Paciente {nombre} registrado con DNI {dni}.")

    def agendar_cita(self, dni, fecha):
        if dni not in self.pacientes:
            print("Paciente no encontrado.")
            return
        self.citas.append({'dni': dni, 'fecha': fecha})
        print(f"Cita agendada para {self.pacientes[dni]} en la fecha {fecha}.")

    def modificar_fecha(self, dni, nueva_fecha):
        for cita in self.citas:
            if cita['dni'] == dni:
                cita['fecha'] = nueva_fecha
                print("Fecha de cita modificada.")
                return
        print("Cita no encontrada.")

    def consultar_citas(self):
        for cita in self.citas:
            paciente = self.pacientes[cita['dni']]
            print(f"Paciente: {paciente}, Fecha: {cita['fecha']}")

    def enviar_recordatorios(self):
        hoy = datetime.date.today()
        for cita in self.citas:
            fecha_cita = datetime.datetime.strptime(cita['fecha'], "%Y-%m-%d").date()
            if 0 < (fecha_cita - hoy).days <= 3:
                print(f"Recordatorio: Cita para {self.pacientes[cita['dni']]} el {cita['fecha']}.")


# Clase para gestión de inventario
class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open('inventario.json', 'r') as file:
                self.productos = json.load(file)
        except FileNotFoundError:
            self.productos = {}

    def guardar_productos(self):
        with open('inventario.json', 'w') as file:
            json.dump(self.productos, file)

    def agregar_producto(self, nombre, categoria, stock):
        self.productos[nombre] = {'categoria': categoria, 'stock': stock}
        self.guardar_productos()
        print(f"Producto {nombre} agregado.")

    def actualizar_stock(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre]['stock'] += cantidad
            self.guardar_productos()
            print(f"Stock de {nombre} actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        producto = self.productos.get(nombre, None)
        if producto:
            print(f"Producto: {nombre}, Categoría: {producto['categoria']}, Stock: {producto['stock']}")
        else:
            print("Producto no encontrado.")

    def reportar_agotados(self):
        print("Productos agotados:")
        for nombre, info in self.productos.items():
            if info['stock'] <= 0:
                print(f"{nombre} - Categoría: {info['categoria']}")


# Clase para gestión de biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.prestamos = {}
        self.cargar_libros()

    def cargar_libros(self):
        try:
            with open('biblioteca.json', 'r') as file:
                self.libros = json.load(file)
        except FileNotFoundError:
            self.libros = {}

    def guardar_libros(self):
        with open('biblioteca.json', 'w') as file:
            json.dump(self.libros, file)

    def registrar_libro(self, titulo, autor):
        self.libros[titulo] = {'autor': autor, 'prestado': False, 'fecha_devolucion': None}
        self.guardar_libros()
        print(f"Libro {titulo} registrado.")

    def prestar_libro(self, titulo, dni):
        if titulo in self.libros and not self.libros[titulo]['prestado']:
            fecha_devolucion = datetime.date.today() + datetime.timedelta(days=14)
            self.libros[titulo]['prestado'] = True
            self.libros[titulo]['fecha_devolucion'] = str(fecha_devolucion)
            self.prestamos[dni] = titulo
            self.guardar_libros()
            print(f"Libro {titulo} prestado a {dni}. Debe devolverse antes de {fecha_devolucion}.")
        else:
            print("Libro no disponible.")

    def devolver_libro(self, dni):
        if dni in self.prestamos:
            titulo = self.prestamos[dni]
            self.libros[titulo]['prestado'] = False
            self.libros[titulo]['fecha_devolucion'] = None
            del self.prestamos[dni]
            self.guardar_libros()
            print(f"Libro {titulo} devuelto por {dni}.")
        else:
            print("No hay libros prestados a este usuario.")

# Función principal
def main():
    sistema_citas = CitaMedica()
    sistema_inventario = Inventario()
    sistema_biblioteca = Biblioteca()

    while True:
        print("\nSeleccione una opción:")
        print("1. Gestión de Citas Médicas")
        print("2. Sistema de Inventario para Tienda")
        print("3. Gestión de Biblioteca")
        print("4. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == '1':
            while True:
                print("\nGestión de Citas Médicas:")
                print("1. Registrar Paciente")
                print("2. Agendar Cita")
                print("3. Modificar Fecha de Cita")
                print("4. Consultar Citas")
                print("5. Enviar Recordatorios")
                print("6. Volver al menú principal")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    nombre = input("Nombre del paciente: ")
                    dni = input("DNI del paciente: ")
                    sistema_citas.registrar_paciente(nombre, dni)
                elif sub_opcion == '2':
                    dni = input("DNI del paciente: ")
                    fecha = input("Fecha de la cita (YYYY-MM-DD): ")
                    sistema_citas.agendar_cita(dni, fecha)
                elif sub_opcion == '3':
                    dni = input("DNI del paciente: ")
                    nueva_fecha = input("Nueva fecha de la cita (YYYY-MM-DD): ")
                    sistema_citas.modificar_fecha(dni, nueva_fecha)
                elif sub_opcion == '4':
                    sistema_citas.consultar_citas()
                elif sub_opcion == '5':
                    sistema_citas.enviar_recordatorios()
                elif sub_opcion == '6':
                    break

        elif opcion == '2':
            while True:
                print("\nSistema de Inventario para Tienda:")
                print("1. Agregar Producto")
                print("2. Actualizar Stock")
                print("3. Buscar Producto")
                print("4. Reportar Productos Agotados")
                print("5. Volver al menú principal")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    nombre = input("Nombre del producto: ")
                    categoria = input("Categoría del producto: ")
                    stock = int(input("Stock del producto: "))
                    sistema_inventario.agregar_producto(nombre, categoria, stock)
                elif sub_opcion == '2':
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("Cantidad a agregar: "))
                    sistema_inventario.actualizar_stock(nombre, cantidad)
                elif sub_opcion == '3':
                    nombre = input("Nombre del producto: ")
                    sistema_inventario.buscar_producto(nombre)
                elif sub_opcion == '4':
                    sistema_inventario.reportar_agotados()
                elif sub_opcion == '5':
                    break

        elif opcion == '3':
            while True:
                print("\nGestión de Biblioteca:")
                print("1. Registrar Libro")
                print("2. Prestar Libro")
                print("3. Devolver Libro")
                print("4. Volver al menú principal")
                
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    titulo = input("Título del libro: ")
                    autor = input("Autor del libro: ")
                    sistema_biblioteca.registrar_libro(titulo, autor)
                elif sub_opcion == '2':
                    titulo = input("Título del libro: ")
                    dni = input("DNI del usuario: ")
                    sistema_biblioteca.prestar_libro(titulo, dni)
                elif sub_opcion == '3':
                    dni = input("DNI del usuario: ")
                    sistema_biblioteca.devolver_libro(dni)
                elif sub_opcion == '4':
                    break

        elif opcion == '4':
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
