# Simulador de Ventas en Línea
class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        return self.precio * (1 - porcentaje / 100)

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self, tasa_impuesto):
        total = sum([producto.precio for producto in self.productos])
        total_con_impuesto = total * (1 + tasa_impuesto / 100)
        return total_con_impuesto

    def resumen_compra(self):
        resumen = {}
        for producto in self.productos:
            if producto.nombre in resumen:
                resumen[producto.nombre] += 1
            else:
                resumen[producto.nombre] = 1
        return resumen


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

    def calcular_total(self, tasa_impuesto):
        total = sum([plato.precio for plato in self.pedidos])
        total_con_impuesto = total * (1 + tasa_impuesto / 100)
        return total_con_impuesto

    def mostrar_cuenta(self):
        cuenta_detallada = {}
        for plato in self.pedidos:
            if plato.nombre in cuenta_detallada:
                cuenta_detallada[plato.nombre] += 1
            else:
                cuenta_detallada[plato.nombre] = 1
        return cuenta_detallada


# Gestión de Flota de Autos
class Auto:
    def __init__(self, modelo, estado):
        self.modelo = modelo
        self.estado = estado

class Flota:
    def __init__(self):
        self.autos = []

    def registrar_auto(self, auto):
        self.autos.append(auto)

    def cambiar_estado(self, modelo, nuevo_estado):
        for auto in self.autos:
            if auto.modelo == modelo:
                auto.estado = nuevo_estado
                return
        print("Auto no encontrado.")

    def consultar_disponibilidad(self):
        return [auto.modelo for auto in self.autos if auto.estado == "disponible"]


# Función principal
def main():
    carrito = Carrito()
    restaurante = {}
    flota = Flota()

    while True:
        print("\nSeleccione una opción:")
        print("1. Simulador de Ventas en Línea")
        print("2. Sistema de Gestión de Restaurante")
        print("3. Gestión de Flota de Autos")
        print("4. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == '1':
            # Simulador de Ventas en Línea
            productos = [
                Producto("Laptop", "Electrónica", 800),
                Producto("Sofá", "Muebles", 300),
                Producto("Cafetera", "Electrodomésticos", 50)
            ]

            while True:
                print("\nSimulador de Ventas en Línea:")
                print("1. Buscar Productos")
                print("2. Agregar al Carrito")
                print("3. Realizar Pago")
                print("4. Volver al menú principal")

                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    categoria = input("Ingrese la categoría o palabra clave: ")
                    resultados = list(filter(lambda p: categoria.lower() in p.nombre.lower() or categoria.lower() in p.categoria.lower(), productos))
                    if resultados:
                        print("Productos encontrados:")
                        for producto in resultados:
                            print(f"{producto.nombre} - {producto.categoria} - ${producto.precio}")
                    else:
                        print("No se encontraron productos.")
                elif sub_opcion == '2':
                    nombre_producto = input("Ingrese el nombre del producto a agregar: ")
                    for producto in productos:
                        if producto.nombre.lower() == nombre_producto.lower():
                            carrito.agregar_producto(producto)
                            print(f"{producto.nombre} agregado al carrito.")
                            break
                    else:
                        print("Producto no encontrado.")
                elif sub_opcion == '3':
                    tasa_impuesto = 10  # Porcentaje de impuestos
                    total = carrito.calcular_total(tasa_impuesto)
                    resumen = carrito.resumen_compra()
                    print("Resumen de la compra:")
                    for nombre, cantidad in resumen.items():
                        print(f"{nombre}: {cantidad}")
                    print(f"Total a pagar: ${total:.2f}")
                    break
                elif sub_opcion == '4':
                    break

        elif opcion == '2':
            # Sistema de Gestión de Restaurante
            while True:
                print("\nSistema de Gestión de Restaurante:")
                print("1. Registrar Mesa")
                print("2. Hacer Pedido")
                print("3. Mostrar Cuenta")
                print("4. Volver al menú principal")

                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    numero_mesa = input("Número de mesa: ")
                    restaurante[numero_mesa] = Mesa(numero_mesa)
                    print(f"Mesa {numero_mesa} registrada.")
                elif sub_opcion == '2':
                    numero_mesa = input("Número de mesa: ")
                    if numero_mesa in restaurante:
                        plato_nombre = input("Nombre del plato: ")
                        precio = float(input("Precio del plato: "))
                        plato = Plato(plato_nombre, precio)
                        restaurante[numero_mesa].agregar_pedido(plato)
                        print(f"Pedido de {plato_nombre} agregado a la mesa {numero_mesa}.")
                    else:
                        print("Mesa no encontrada.")
                elif sub_opcion == '3':
                    numero_mesa = input("Número de mesa: ")
                    if numero_mesa in restaurante:
                        total = restaurante[numero_mesa].calcular_total(10)  # Porcentaje de impuestos
                        cuenta = restaurante[numero_mesa].mostrar_cuenta()
                        print(f"Cuenta de la mesa {numero_mesa}:")
                        for plato, cantidad in cuenta.items():
                            print(f"{plato}: {cantidad}")
                        print(f"Total a pagar: ${total:.2f}")
                    else:
                        print("Mesa no encontrada.")
                elif sub_opcion == '4':
                    break

        elif opcion == '3':
            # Gestión de Flota de Autos
            while True:
                print("\nGestión de Flota de Autos:")
                print("1. Registrar Auto")
                print("2. Cambiar Estado de Auto")
                print("3. Consultar Disponibilidad")
                print("4. Volver al menú principal")

                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == '1':
                    modelo = input("Modelo del auto: ")
                    estado = input("Estado del auto (disponible/alquilado/mantenimiento): ")
                    auto = Auto(modelo, estado)
                    flota.registrar_auto(auto)
                    print(f"Auto {modelo} registrado.")
                elif sub_opcion == '2':
                    modelo = input("Modelo del auto: ")
                    nuevo_estado = input("Nuevo estado del auto (disponible/alquilado/mantenimiento): ")
                    flota.cambiar_estado(modelo, nuevo_estado)
                elif sub_opcion == '3':
                    disponibles = flota.consultar_disponibilidad()
                    if disponibles:
                        print("Autos disponibles:")
                        for auto in disponibles:
                            print(auto)
                    else:
                        print("No hay autos disponibles.")
                elif sub_opcion == '4':
                    break

        elif opcion == '4':
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
