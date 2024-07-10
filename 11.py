nombre=[]
aux=""
for i in range(3):
    nombre.append(input("Ingrese nombre "))
if len(nombre[i])> len(aux):
    aux=nombre[i]
print("el nombre con mas caracteres es", aux)
x=min(nombre)
print("el nombre con mas caracteres es", x)
# nombre_largo= max(nombre, Key=len)
# print(f"el nombre largo es {nombre_largo}")