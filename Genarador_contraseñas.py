import random
palabra = input("Ingresa tu nombre : ")

def Letras_palabra_random(palabra):
    palabra = list(palabra)
    letras = [random.choice(palabra) for i in range(5)]
    unir = ''.join(letras)
    return unir

print(Letras_palabra_random(palabra))

def Numeros_random():
    numero = random.randint(0, 1000)
    texto = str(numero)
    return texto

print(Numeros_random())
def Random_Caracteres():
    non_alphanumeric_chars = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~', '¡', '¿', 
    ]
    caracter = [random.choice(non_alphanumeric_chars) for i in range(5)]
    unir = ''.join(caracter)
    return unir

print(Random_Caracteres())

def Genarar_contrasena(palabra):
    beta = Letras_palabra_random(palabra)
    gamma = Numeros_random()
    alpha = Random_Caracteres()
    contra =[beta, gamma, alpha]
    letras = [random.choice(contra) for i in range(4)]
    unir = ''.join(letras)
    return unir

print(Genarar_contrasena(palabra))
