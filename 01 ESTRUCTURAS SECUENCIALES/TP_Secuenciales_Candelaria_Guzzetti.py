# Trabajo realizado por Candelaria Guzzetti

# Ejercicio 1

print ("Hola Mundo!")

# Ejercicio 2

nombre = input("Ingrese su nombre ")

print (f"Hola {nombre}! ")

# Ejercicio 3

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
lugar_residencia = input("Ingrese su lugar de residencia ")

print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# Ejercicio 4 

radio = int(input("¿Cuál es el radio en centímetros del circulo a analizar? "))
diametro = 2 * float(3.14) * radio
area = float(3.14) * (radio)**2
print (f"El diametro de ese radio es {diametro} centimetros y su área es {area} centimetros")

#Ejercicio 5

segundos = int(input("Ingresa el número de segundos que querés convertir a horas "))
resultado = (segundos/3600)
print (f"{segundos} segundos son {resultado} horas")

#Ejercicio 6

numero = int(input("¿De qué numero querés saber la tabla de multiplicar? "))
tabla2 = (numero * 2)
tabla3 = (numero * 3)
tabla4 = (numero * 4)
tabla5 = (numero * 5)
tabla6 = (numero * 6)
tabla7 = (numero * 7)
tabla8 = (numero * 8)
tabla9 = (numero * 9)
tabla10 = (numero * 10)
print (f"{numero} X 2 = {tabla2}, {numero} X 3 = {tabla3}, {numero} X 4 = {tabla4}, {numero} X 5 = {tabla5}, {numero} X 6 = {tabla6}, {numero} X 7 = {tabla7}, {numero} X 8 = {tabla8}, {numero} X 9 = {tabla9}, {numero} X 10 = {tabla10}")

# Ejercicio 7

num1 = int(input("Dame el primer número entero mayor a cero que quieras calcular "))
num2 = int(input("Dame el segundo número entero mayor a cero que quieras calcular "))
suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = (num1 * num2)
division = (num1 / num2)
print (f"Los resultados entre las operaciones entre {num1} y {num2} son los siguientes: Suma: {suma}, Resta {resta}, Multiplicación {multiplicacion}, División {division}")

# Ejercicio 8 

peso = float(input("¿Cuál es tu peso en kilogramos? "))
altura = float(input("¿Cuál es tu altura en metros? "))
imc = peso / (altura)**2
print (f"Tu IMC es {imc}")

# Ejercicio 9 

celsius = int(input("Ingresa los grados en Celsius que quieras convertir a Fahrenheit "))
fahrenheit = float(1.8) * celsius + 32
print (f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit")

# Ejercicio 10

num1 =int(input("Dame el primer número a promediar "))
num2 =int(input("Dame el segundo número a promediar "))
num3 =int(input("Dame el tercer número a promediar "))
resultado = (num1 + num2 + num3) / 3
print (f"El promedio de {num1}, {num2} y {num3} es {resultado}")
