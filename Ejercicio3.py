import time

inventario = {
    "Laptop" : 10,
    "Mouse" : 25,
    "Teclado" : 15
}

while True:
    print("*** SISTEMA DE INVENTARIO TITAN ***")
    print("1.- Mostrar productos disponibles.")
    print("2.- Realizar una venta.")
    print("3.- Salir.")
    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print("ERROR!! debe ingresar un número entero válido")
        time.sleep(1.5)    
        continue
    if opc == 1:
        print("--- PRODUCTOS EN STOCK ---")
        for producto, stock in inventario.items():
            print(f"- {producto}: {stock} unidades.")
        input("Presione para volver al menú...")    
    if opc == 2:
        print("")    