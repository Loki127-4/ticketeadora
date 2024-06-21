import secrets
import string
import sys

diccionario = {
    "letras": string.ascii_letters,
    "numeros": string.digits,
    "caracteres": string.punctuation
}

def generar_password(longitud, tipos):
    caracteres = "".join([diccionario[tipo] for tipo in tipos])
    contrasena = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = 8 
tipos = ["letras", "numeros", "caracteres"]  

contrasena = generar_password(longitud, tipos)
print("Contraseña generada:", contrasena)
