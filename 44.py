# Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la
# opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para
# confirmar la eliminación, deberán escribir la contraseña correspondiente de cada
# usuario.
# 1. Inicio sesión.
# 2. Registrar usuario
# 3. Eliminar usuario.
# 4. Salir.
# La opción 1 solo mostrará un mensaje exitoso si ha iniciado correctamente,
# o un error de caso contrario

usuario=[]
contraseña=[]
while True:
    print(" 1. Iniciar sesion \n 2. Registrar usuario \n 3. Eliminar usuario \n 4. Salir")
    opc=int(input("Ingrese opcion "))
    if opc==1:
        user=input("Ingrese usuario ")
        pas= input("Ingrese contraseña ")
        if (user in usuario) and (pas in contraseña):
            print("Sesion iniciada")
        else:
            print("Usuario no registrado")
    elif opc==2:
        usuario.append(input("Ingrese nuevo usuario: "))
        contraseña.append(input("Ingrese nueva contraseña: "))
    elif opc==3:
        user=(input("Ingrese usuario a eliminar "))
        for i in range (len(usuario)):
            if user==usuario[i]: 
                usuario.remove(usuario)
                contraseña.remove(contraseña)
    elif opc==4:
        break
        
        
        