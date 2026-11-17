contrasena = "Hola1234"
print(contrasena)


def comprobar_longitud(contrasena):
  return len(contrasena) >= 8


def comprobar_mayuscula(contrasena):
  return any(caracter.isupper() for caracter in contrasena)


print("Longitud válida:", comprobar_longitud(contrasena))
print("¿Contiene mayúsculas? (fija):", comprobar_mayuscula(contrasena))
print(
    "Prueba sin mayúsculas ('hola1234'):", comprobar_mayuscula("hola1234")
)
print(
    "Prueba con mayúsculas ('HOLA1234'):", comprobar_mayuscula("HOLA1234")
)