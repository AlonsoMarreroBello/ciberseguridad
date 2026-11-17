contrasena = "Hola1234"
print(contrasena)


def comprobar_longitud(contrasena):
  return len(contrasena) >= 8


# Llamada con la contraseña fija y pruebas
print("Contraseña fija:", comprobar_longitud(contrasena))
print("Prueba < 8 caracteres ('abc'):", comprobar_longitud("abc"))
print(
    "Prueba >= 8 caracteres ('ContrasenaSegura'):",
    comprobar_longitud("ContrasenaSegura"),
)