# Trabajo realizado por Candelaria Guzzetti

while True: 
    ejercicio = int (input ("¿Qué número de ejercicio desea ver? (1-10) "))
    if ejercicio == 1:
        
        def imprimir_hola_mundo():
            print ("Hola Mundo!")

        imprimir_hola_mundo()

    elif ejercicio == 2:
        
        def saludar_usuario(nombre):
            print (f"Hola {nombre}!")

        nombre = input ("¿Cuál es tu nombre? ")

        saludar_usuario(nombre)

    elif ejercicio == 3:
        
        
        def informacion_personal(nombre, apellido, edad, residencia):
            print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

        nombre = input ("¿Cuál es su nombre? ")
        apellido = input ("¿Cuál es su apellido? ")
        edad = input ("¿Cuál es su edad? ")
        residencia = input ("¿Cuál es su lugar de residencia? ")

        informacion_personal(nombre, apellido, edad, residencia)

    elif ejercicio == 4:
        
        def calcular_area_circulo(radio):
            area = 3.14 * radio**2
            return area

        def calcular_perimetro_circulo(radio):
            perimetro = 2 * 3.14 * radio
            return perimetro

        radio = int (input ("Ingrese el radio del círculo para calcular su área y perímetro "))

        perimetro = calcular_perimetro_circulo(radio)

        area = calcular_area_circulo (radio)

        print (f"El perímetro es {perimetro} y el área es {area}")

    elif ejercicio == 5:
        
        def segundos_a_horas(segundos):
            resultado = (segundos/3600)
            return resultado
        
        segundos = int (input ("Ingrese la cantidad de segundos que quiere convertir en horas "))
        print (f"{segundos} segundos son {segundos_a_horas(segundos)} horas")

    elif ejercicio == 6:
        
        def tabla_multiplicar(numero):
            tabla1 = (numero * 1)
            tabla2 = (numero * 2)
            tabla3 = (numero * 3)
            tabla4 = (numero * 4)
            tabla5 = (numero * 5)
            tabla6 = (numero * 6)
            tabla7 = (numero * 7)
            tabla8 = (numero * 8)
            tabla9 = (numero * 9)
            tabla10 = (numero * 10)

            print (f"{numero} X 1 = {tabla1}, {numero} X 2 = {tabla2}, {numero} X 3 = {tabla3}, {numero} X 4 = {tabla4}, {numero} X 5 = {tabla5}, {numero} X 6 = {tabla6}, {numero} X 7 = {tabla7}, {numero} X 8 = {tabla8}, {numero} X 9 = {tabla9}, {numero} X 10 = {tabla10}")
        
        numero = int (input ("Elija un número para hacer su tabla del 1 al 10 "))

        tabla_multiplicar(numero)

    elif ejercicio == 7:
        lista = ()

        def operaciones_basicas(a, b):
            suma = (a + b)
            resta = (a - b)
            multiplicacion = (a * b)
            division = (a / b)

            resultado = suma, resta, multiplicacion, division

            return resultado
        
        a = int(input("Dame el primer número entero mayor a cero que quieras calcular "))
        b = int(input("Dame el segundo número entero mayor a cero que quieras calcular "))

        resultado = operaciones_basicas(a, b)

        print (f"{a} + {b} = {resultado [0]}, {a} - {b} = {resultado [1]}, {a} * {b} = {resultado [2]}, {a} / {b} = {resultado [3]}")

    elif ejercicio == 8:

        def calcular_imc(peso, altura):
            imc = peso / (altura)**2
            return imc
        
        peso = float(input("¿Cuál es tu peso en kilogramos? "))
        altura = float(input("¿Cuál es tu altura en metros? "))
        
        print (f"Tu IMC es {calcular_imc(peso, altura)}")
        
    elif ejercicio == 9:

        def celsius_a_fahrenheit(celsius):
            fahrenheit = float(1.8) * celsius + 32
            return fahrenheit
        
        celsius = int(input("Ingresa los grados en Celsius que quieras convertir a Fahrenheit "))
        
        print (f"{celsius} grados Celsius son equivalentes a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")


    elif ejercicio == 10:
        
        def calcular_promedio(a, b, c):
            resultado = (a + b + c) / 3
            return resultado
        
        a =int(input("Dame el primer número a promediar "))
        b =int(input("Dame el segundo número a promediar "))
        c =int(input("Dame el tercer número a promediar "))
        
        print (f"El promedio de {a}, {b} y {c} es {calcular_promedio(a, b, c)}")

    else:
        print ("No seleccionó un número del 1 al 10")