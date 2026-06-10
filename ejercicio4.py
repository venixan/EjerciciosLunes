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

suma_total=sum(numeros)
cantidad_num=len(numeros)
promedio=suma_total/cantidad_num

print(f"---Resultados---")
print(f"La lista completa es: {numeros}")
print(f"La suma total es: {suma_total}")
print(f"El promedio es: {promedio}")        
