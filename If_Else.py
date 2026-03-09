# -----if- Else ---------
Codigo_acceso = 1234
Codigo_ingresado = int(input("Escribe el codigo de acceso:  "))
if Codigo_ingresado == Codigo_acceso:
   print("Acceso autorizado")
else:
   print("Intente nuevamente")
   # SEGUNDO EJMPLO -----
   codigo_acceso = 12345
   codigo_ingresado = int(input(" ingrese su codigo:  "))
   if Codigo_ingresado == codigo_acceso:
      print("Acceso Permitido")
   else: 
      print("Intente de nuevo")
#-------tercer ejempplo-----
codigo_acceso = 1234
intentos = 0
codigo_ingresado = int(input("Ingrsa el codigo:  "))
while intentos < 3:
   if codigo_ingresado == codigo_acceso:
      print("Acceso autorizado")
   break
else: 
      print("intente nuevamente")
intentos = intentos + 1
   