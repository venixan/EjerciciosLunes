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
        print("--- NUEVA VENTA ---")
        productoa_vender = input("Ingrese el nombre del producto: ").strip().title()
        if productoa_vender not in inventario:
            print("ERROR!! el producto que usted selecciono no esta en el inventario.")
            time.sleep(1.8)
            continue
        while True:
            try:
                Cantidad_venta=int(input(f"¿cuantas unidades de {producto} desea llevar?: "))
                if Cantidad_venta>0:
                    break
                else:
                    print("Error!! la cantidad debe ser mayor a 0!!")
            except ValueError:
                print("ERROR!! debe ingresar un número entero válido.")  
        stock_actual= inventario[productoa_vender]
        
