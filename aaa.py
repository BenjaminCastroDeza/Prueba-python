def verificar_numero(num):
    if num < 0:
        return "Número negativo"
    return "Número positivo o cero"

print(verificar_numero(-10))  # Output: Número positivo o cero
print(verificar_numero(-5))  # Output: Número negativo