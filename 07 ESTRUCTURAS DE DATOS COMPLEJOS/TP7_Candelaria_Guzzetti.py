# Trabajo realizado por Candelaria Guzzetti

while True: # Condicion para que se pueda repetir el selector de ejercicios una vez revisados

    ejercicio = input ("Introduzca el número de ejercicio del 1 al 13 ") 

    match ejercicio:
        case "1": #Ejercicio 1

            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

            precios_frutas["Naranja"] = 1200
            precios_frutas["Manzana"] = 1500
            precios_frutas["Pera"] = 2300

            print (precios_frutas)

        case "2":
            
            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

            precios_frutas["Naranja"] = 1200
            precios_frutas["Manzana"] = 1500
            precios_frutas["Pera"] = 2300

            precios_frutas["Banana"] = 1300
            precios_frutas["Manzana"] = 1700
            precios_frutas["Melón"] = 2800

            print (precios_frutas)
        
        case "3":

            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

            precios_frutas["Naranja"] = 1200
            precios_frutas["Manzana"] = 1500
            precios_frutas["Pera"] = 2300

            precios_frutas["Banana"] = 1300
            precios_frutas["Manzana"] = 1700
            precios_frutas["Melón"] = 2800

            frutas = precios_frutas.keys()

            print (frutas)

        case "4":
        
            nombre_y_numeros = {}

            for n in range (5):
                
                nombre = input ("Ingrese el nombre de la persona a agendar ")

                numero = input ("Ingrese el número de teléfono de la persona a agendar ")

                nombre_y_numeros[nombre] = numero

            nombre_pedido = input ("Ingrese el nombre a buscar")

            busqueda = nombre_y_numeros[nombre_pedido]

            print (busqueda)

        case "5":
            
            frase = input ("Ingrese una frase ")

            palabras = frase.split()

            palabras_unicas = set(palabras)

            print (palabras_unicas)

            lista_palabras = list(palabras_unicas)

            dicc_palabras = dict()

            contador = 0

            for c in range (len(lista_palabras)):
                for lista_palabras[c] in lista_palabras:
                    contador += 1 
                    dicc_palabras[lista_palabras[c]] = contador
                contador = 0

            print (dicc_palabras)

        case "6":

            alumno = dict()

            for n in range (3):

                nombre = input (f"Ingrese el nombre del alumno {n+1} ")

                tupla = tuple ()

                alumnos = []

                for m in range (3):
                    nota = input (f"Ingrese la nota {m+1} ")

                    tupla = tupla + (nota,)

                alumno[nombre] =  tupla

                alumnos.append(alumno)                

            print (alumnos)

        case "7":

            asistencias = ["Ana", "Luis", "Maria", "Luis", "Pedro", "Ana"]

            print (asistencias)
            
            set_asistencias = set()

            set_asistencias.update(asistencias)

            print (set_asistencias)

            dicc_asistencias = dict()

            contador = 0
            
            for nombre in asistencias:
                if nombre in dicc_asistencias:
                    dicc_asistencias[nombre] += 1
                else:
                    dicc_asistencias[nombre] = 1
                
            print (dicc_asistencias)

        case "8":
            
            inventario = {"Martillos" : 100, "Destornilladores" : 200, "Espatulas" : 150}

            producto = input("Ingrese el nombre del producto que quiere consultar ")

            if producto in inventario:

                print(f"Hay {inventario[producto]} unidades de {producto}")

                agregar = input ("¿Desea agregar más unidades de stock? Presione 1 para SI o 2 para NO. ")

                match agregar:

                    case "1":

                        unidades = input ("¿Cuántas unidades desea agregar? ")

                        stock_actualizado = inventario[producto] + int(unidades)
                        
                        inventario[producto] = stock_actualizado

                        print(f"Ahora hay {inventario[producto]} unidades de {producto}")

                    case "2":
                        break
                    case _:
                        print ("Por favor ingrese 1 para SI o 2 para NO. ")

            else:
                print ("Ese producto no se encuentra dentro del inventario")

                nuevo_pregunta = input ("¿Desea agregar un nuevo producto? Presione 1 para SI o 2 para NO. ")

                match nuevo_pregunta:

                    case "1":
                        nuevo_producto = input ("Ingrese el nomnre del nuevo producto que quiere agregar ")

                        nuevo_stock = input ("Ingrese el stock asociado a ese producto" )

                        inventario[nuevo_producto] = nuevo_stock

                        print ("El inventario se ha actualizado.")

                    case "2":
                        break

                    case _:
                        print ("Por favor ingrese 1 para SI o 2 para NO.")
        
        case "9":
            
            agenda = {}

            while True:

                accion = input ("Elija la acción a realizar: 1) Agregar eventos // 2) Consultar eventos. ")

                dia_hora = ()

                if accion == "1":
                    
                    dia = input ("Ingrese el día del evento. ").strip().lower()

                    hora = input ("Ingrese la hora del evento. ").strip()

                    evento = input ("Ingrese el evento correspondiente. ")

                    agenda[(dia, hora)] = evento

                elif accion == "2":

                    dia_consulta = input ("Ingrese el día del evento a consultar. ").strip().lower()

                    hora_consulta = input ("Ingrese la hora del evento a consultar. ").strip()

                    dia_hora_consulta = (dia_consulta, hora_consulta)

                    if dia_hora_consulta in agenda:

                        print (f"El evento de esa dia y hora es el siguiente: {agenda[dia_hora_consulta]}.")

                    else:
                        print("No hay evento en ese día y hora")    

                else:
                    print ("Por favor ingrese 1) Agregar eventos // 2) Consultar eventos. ")

            
        case "10":
            
            paises = {"Argentina ": "Buenos Aires", "Chile" : "Santiago", "Uruguay" : "Montevideo", "Venezuela" : "Caracas"}

            print (paises)

            capitales = {}

            for pais, capital in paises.items():
                capitales[capital] = pais

            print(capitales)



        case _:
            print ("Ingrese un número del 1 al 10.")