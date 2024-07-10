#Escribe una función llamada area_rectangulo que tome el ancho y el alto de un rectángulo como parámetros y devuelva su 
#área. Luego, pide al usuario el ancho y el alto y usa la función para mostrar el área.

def registrar_trabajador(trabajadores):
    CARGOS = ["Gerente", "Ingeniero", "Analista", "Administrativo"]  # Definir cargos válidos
    nombre = input("Ingrese nombre: ")
    cargo = input("Ingrese cargo: ")
    
    while cargo not in CARGOS:
        print("Ingrese cargo válido")
        cargo = input("Ingrese cargo: ")
    
    sueldobruto = int(input("Ingrese sueldo: "))
    
    trabajador = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldobruto": sueldobruto
    }
    
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente")

# Lista para almacenar los trabajadores
trabajadores = []

# Llamar a la función para registrar un trabajador
registrar_trabajador(trabajadores)

# Mostrar la lista de trabajadores registrados
print(trabajadores)