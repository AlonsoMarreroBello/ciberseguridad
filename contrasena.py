from utilidades import comprobar_numero

contrasena = "Hola1234"
print(contrasena)


def comprobar_longitud(contrasena):
  return len(contrasena) >= 12


def comprobar_mayuscula(contrasena):
  return any(caracter.isupper() for caracter in contrasena)


print("1. Longitud (>=8):", comprobar_longitud(contrasena))
print("2. Contiene números:", comprobar_numero(contrasena))
print("3. Contiene mayúsculas:", comprobar_mayuscula(contrasena))