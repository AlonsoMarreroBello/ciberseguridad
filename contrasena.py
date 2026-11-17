from utilidades import comprobar_numero

contrasena = "Hola1234"
print(contrasena)


def comprobar_longitud(contrasena):
  return len(contrasena) >= 8


print("Longitud válida:", comprobar_longitud(contrasena))
print("¿Contiene números? (fija):", comprobar_numero(contrasena))
print("Prueba sin números ('Hola'):", comprobar_numero("Hola"))
print("Prueba con números ('Clave123'):", comprobar_numero("Clave123"))