# Trabajo realizado por Candelaria Guzzetti

# Ejercicio 1 

edad = int(input("Ingrese su edad "))
if edad >= 18:
    print ("Es mayor de edad")
print ("Chau")

# Ejercicio 2 

nota = int(input("¿Cuál fue tu nota? "))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

# Ejercicio 3

numero = int(input("Ingrese un número entero "))
if numero%2 == 0:
    print  ("Ha ingresado un número par")
else: 
    print ("Por favor, ingrese un número par")

# Ejercicio 4 

edad = int(input("¿Cuál es tu edad?"))
if edad <12:
    print ("Usted es un/a niño/a")
elif edad >= 12 and edad < 18:
    print ("Usted es un/a adolescente")
elif edad >= 18 and edad < 30:
    print ("Usted es un/a adulto/a joven")
else:
    print ("Usted es un/a adulto/a")

# Ejercicio 5

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres ")
longitud = (len(contraseña))
if longitud >= 8 and longitud <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6 

consumo = int(input("¿Cuál es su consumo mensual de energía eléctrica en kilovatios (kWh)? "))
if consumo < 150:
    print("Consumo bajo")
elif consumo >= 150 and consumo <= 300:
    print ("Consumo medio")
else:
    print ("Consumo alto")

if consumo > 500:
    print ("Considere medidas de ahorro energético")

# Ejercicio 7

frase = input("Ingrese una frase o palabra ")
if frase [-1].lower() in 'aeiou':
    print (f"{frase}!")
else:
    print (f"{frase}")

#Ejercicio 8

nombre = input("Ingrese su nombre ")
opcion = int(input("Seleccione 1. Si quiere su nombre en mayúsculas, 2. Si quiere su nombre en minúsculas, 3. Si quiere su nombre con la primera letra mayúscula "))

match opcion:
    case 1:
        print (f"{nombre.upper()}")
    case 2: 
        print (f"{nombre.lower()}")
    case 3:
        print (f"{nombre.title()}")
    case _:
        print ("Ingrese un número del 1 al 3 por favor")

# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto "))
if magnitud < float(3):
    print ("El terremoto fue Muy leve (imperceptible).")
elif magnitud >= float(3) and magnitud < float(4):
    print ("El terremoto fue Leve (ligeramente perceptible).")
elif magnitud >= float(4) and magnitud < float(5):
    print ("El terremoto fue Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= float(5) and magnitud < float(6):
    print ("El terremoto fue Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= float(6) and magnitud < float(7):
    print ("El terremoto fue Muy Fuerte (puede causar daños significativos).")
else:
    print ("El terremoto fue Extremo (puede causar graves daños a gran escala.")

# Ejercicio 10

hemisferio = input ("¿En que hemisferio se encuentra actualmente? (Norte/Sur) ").lower()
mes = input("¿En que mes está?").lower()
dia = int(input("¿Qué día (número) es?"))
if (((hemisferio == 'norte') and (mes == 'diciembre') and (dia >= 21 and dia <= 31 )) or ((hemisferio == 'norte') and (mes == 'enero') and (dia >= 1 and dia <= 30)) or ((hemisferio == 'norte') and (mes == 'febrero') and (dia >= 1 and dia <= 29)) or ((hemisferio == 'norte') and (mes == 'marzo') and (dia >= 1 and dia <= 20)) or ((hemisferio == 'sur') and (mes == 'junio') and (dia >= 21 and dia <= 30)) or ((hemisferio == 'sur') and (mes == 'julio') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'sur') and (mes == 'agosto') and (dia >= 1 and dia <= 31))  or ((hemisferio == 'sur') and (mes == 'septiembre') and (dia >= 1 and dia <= 20))):
    print ("Usted se encuentra en Invierno")
elif (((hemisferio == 'norte') and (mes == 'marzo') and (dia >= 21 and dia <= 31 )) or ((hemisferio == 'norte') and (mes == 'abril') and (dia >= 1 and dia <= 30)) or ((hemisferio == 'norte') and (mes == 'mayo') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'norte') and (mes == 'junio') and (dia >= 1 and dia <= 20)) or ((hemisferio == 'sur') and (mes == 'septiembre') and (dia >= 21 and dia <= 30)) or ((hemisferio == 'sur') and (mes == 'octubre') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'sur') and (mes == 'noviembre') and (dia >= 1 and dia <= 30)) or ((hemisferio == 'sur') and (mes == 'diciembre') and (dia >= 1 and dia <= 20))):
    print ("Usted se encuentra en Primavera")
elif (((hemisferio == 'norte') and (mes == 'junio') and (dia >= 21 and dia <= 30 )) or ((hemisferio == 'norte') and (mes == 'julio') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'norte') and (mes == 'agosto') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'norte') and (mes == 'septiembre') and (dia >= 1 and dia <= 20)) or ((hemisferio == 'sur') and (mes == 'diciembre') and (dia >= 21 and dia <= 31)) or ((hemisferio == 'sur') and (mes == 'enero') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'sur') and (mes == 'febrero') and (dia >= 1 and dia <= 29)) or ((hemisferio == 'sur') and (mes == 'marzo') and (dia >= 1 and dia <= 20))):
    print ("Usted se encuentra en Verano")
elif (((hemisferio == 'norte') and (mes == 'septiembre') and (dia >= 21 and dia <= 30 )) or ((hemisferio == 'norte') and (mes == 'octubre') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'norte') and (mes == 'noviembre') and (dia >= 1 and dia <= 30)) or ((hemisferio == 'norte') and (mes == 'diciembre') and (dia >= 1 and dia <= 20)) or ((hemisferio == 'sur') and (mes == 'marzo') and (dia >= 21 and dia <= 31)) or ((hemisferio == 'sur') and (mes == 'abril') and (dia >= 1 and dia <= 30)) or ((hemisferio == 'sur') and (mes == 'mayo') and (dia >= 1 and dia <= 31)) or ((hemisferio == 'sur') and (mes == 'junio') and (dia >= 1 and dia <= 20))):
    print ("Usted se encuentra en Otoño")
else:
    print ("Revise los datos ingresados y vuelva a intentarlo")

