import datetime

def caja_registradora():
    print("Caja Registradora")

    productos = []
    total = 0
    while True:
        nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        productos.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio})
        total += cantidad * precio

    tarjeta_fidelizacion = input("¿Tiene tarjeta de fidelización? (s/n): ")
    if tarjeta_fidelizacion.lower() == 's':
        descuento = total * 0.1  # 10% de descuento
        total -= descuento

    print("Recibo:")
    for producto in productos:
        print(f"{producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: {producto['precio']}")
    print(f"Total: {total}")

def carrito_compras():
    print("Carrito de Compras")
    # Implementación básica
    carrito = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == 'salir':
            break
        cantidad = int(input("Ingrese la cantidad: "))
        carrito.append({'producto': producto, 'cantidad': cantidad})

    print("Productos en el carrito:")
    for item in carrito:
        print(f"{item['producto']} - Cantidad: {item['cantidad']}")

def reserva_hotel():
    print("Reserva de Hotel")
    # Implementación básica
    fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
    fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
    tipo_habitacion = input("Ingrese el tipo de habitación (simple/doble/suite): ")

    # Lógica para calcular costo (simplificada)
    costo_noche = {'simple': 100, 'doble': 150, 'suite': 200}
    fecha_ingreso_dt = datetime.datetime.strptime(fecha_ingreso, '%Y-%m-%d')
    fecha_salida_dt = datetime.datetime.strptime(fecha_salida, '%Y-%m-%d')
    noches = (fecha_salida_dt - fecha_ingreso_dt).days

    total = noches * costo_noche[tipo_habitacion]
    print(f"Costo total de la estadía: {total}")

# Más funciones para otros ejercicios...

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Caja Registradora")
        print("2. Carrito de Compras")
        print("3. Reserva de Hotel")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            caja_registradora()
        elif opcion == 2:
            carrito_compras()
        elif opcion == 3:
            reserva_hotel()
        elif opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
