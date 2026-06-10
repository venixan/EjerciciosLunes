notas = {
    "Pedro" : 5.5,
    "María" : 6.2,
    "Juan" :4.8,
    "Ana" : 7.0
}
print("--- SISTEMA DE CONSULTA DE NOTAS ---")

nombre_buscar = input("Ingrese el nombre del alumno a consultar: ").strip().title()
if nombre_buscar in notas:
    alumno_nota = notas[nombre_buscar]
    print(f"La nota de {nombre_buscar} es: {alumno_nota}")
    if alumno_nota >=4.0:
        print("APROBADO!!")
    else:
        print("REPROBADO :C")    
else:
    print("Alumno no encontrado!! ") 

print("Gracias por utilizar el Sistema de notas! hasta luego")       