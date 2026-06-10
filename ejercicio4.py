numeros=[]
print("--- PROMEDIO DE NÚMEROS ---")
for x  in range(5):
    while True:
        try:
            num=int(input(f"Ingrese número entero {x+1}: "))
            break
        except ValueError:
            print("ERROR!! ingrese un número entero valido.")

    numeros.append(num)

        
