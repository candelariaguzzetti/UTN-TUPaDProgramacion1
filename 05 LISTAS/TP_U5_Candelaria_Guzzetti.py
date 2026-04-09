# Trabajo realizado por Candelaria Guzzetti

while True: # Condicion para que se pueda repetir el selector de ejercicios una vez revisados

    ejercicio = input ("Introduzca el número de ejercicio del 1 al 13 ") 

    match ejercicio:
        case "1": # Ejercicio 1
            notas = [4.58, 5.20, 8.88, 7.29, 9.76, 6.77, 8.15, 5.87, 6.61, 3.64] # Cargamos las 10 notas a utilizar en una lista
            notas_promedio = 0 # Creamos la variable donde vamos a cargar el promedio de notas

            notas.sort() #Usamos el método sort para poner en orden numérico las notas
            
            for i in notas: # Recorremos la lista de notas que se va cargando en la variable i
                notas_promedio += i # Sumamos a la variable previamente creada el valor de i (cada item de la lista) para que se sume por completo la lista
            
            promedio = notas_promedio / 10 # Creamos la variable "promedio" y le asignamos el valor de las notas sumadas y lo dividimos por 10 (la cantidad de notas en la lista)

            print (f"{notas}") # Ahora las notas se imprimirán en orden
            print (f"El promedio de dichas notas es: {promedio}") # Mostramos el promedio
            print (f"La notas más baja es {notas[0]}, y la más alta {notas[9]}") # Calculamos la nota más baja y más alta usando los índices de la lista y sabiendo que está en orden y siempre el 0 será más bajo y el 9 más alto

        case "2": # Ejercicio 2
            cont = 0 # Preparamos el contador para que se sepa el número de producto a cargar
            lista = [] # Preparamos la lista vacía que vamos a llenar luego
            for x in range (5): # Hacemos un ciclo que se repita 5 veces para cargar 5 productos como pide la consigna
                cont += 1 # Actualizamos el contador para que funcione correctamente
                producto = input (f"Ingrese el producto {cont} que quiera cargar ") # Pedimos los productos a cargar del 1 al 5
                lista.append (producto) # Vamos agregando a la lista previamente creada los elementos del input
            
            lista.sort() # Ponemos los elementos de la lista en orden alfabetico
            print (f"{lista}") # Imprimimos la lista para que se pueda ver cómo está quedando
            
            deseo = input("¿Desea eliminar algún producto? S para si, N para no ") # Creamos un nuevo input para editar o no la lista
            if deseo == "s" or deseo == "S": # Si ponen estas variables que significan "Si"...
                eliminado = input ("¿Qué producto desea eliminar? ") # ... Creamos otro input para saber que producto quieren eliminar 
                lista.remove(eliminado) # Usamos el método remove para encontrar un coincidencia y eliminarlo 
                print (f"{lista}") # Imprimimos la lista actualizada
            elif deseo == "N" or deseo =="n": # Si ponen estas variables que significan "Si"...
                print ("No elimina nada") # Imprimimos un mensaje para confirmar su decisión 
                break # Y terminamos el programa
            else:
                print ("No eligió S o N") # Avisamos que está mal la elección

        case "3": # Ejercicio 3
            import random # Importamos el módulo random para que nos ayude a elegir al azar los números

            lista = [] # Preparamos las 3 listas que vamos a necesitar llenar luego
            listapares = []
            listaimpares = []

            for j in range (15): # Queremos un ciclo de 15 vueltas
                lista.append (random.randint(1, 100)) # Con el método "Append" vamos llenando la lista con los 15 números aleatorios

            print (f"{lista}") # Imprimimos la lista para ver cómo quedó 

            for l in lista: # Recorremos la lista de notas que se va cargando en la variable l
                if l % 2 == 0:
                    listapares.append (l) # Si el modulo del numero da cero cuando es dividido por 2, entonces ese número es par y lo anexamos a la lista de pares
                elif l % 2 != 0:
                    listaimpares.append (l) # Si el modulo del numero NO da cero cuando es dividido por 2, entonces ese número es impar y lo anexamos a la lista de impares

            print (f"pares: {listapares} / impares: {listaimpares}") # Imprimos los resultados de cada lista

        case "4": # Ejercicio 4
            datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

            cont1 = datos.count (1) # Contamos cuantas veces esta cada número en la lista y lo guardamos en sus respectivas variables para cada número

            cont2 = datos.count (3)

            cont3 = datos.count (5)

            cont4 = datos.count (7)

            cont5 = datos.count (9)

            for x in range (cont1 - 1): # El contador muestra todas las veces que está asi que le restamos 1 para asegurarnos de que quede un solo número
                datos.remove (1) # Removemos todos los números que el contador reconoce menos 1

            for x in range (cont2 - 1): # Hacemos el mismo proceso para todos los números
                datos.remove (3)

            for x in range (cont3 - 1):
                datos.remove (5)

            for x in range (cont4 - 1):
                datos.remove (7)

            for x in range (cont5 - 1):
                datos.remove (9)

            print (f"{datos}") # Imprimimos la lista final sin repeticiones

        case "5": # Ejercicio 5
            
            estudiantes = ["María Perez", "Juana Lopez", "Anabella Gutierrez", "Marisa Ramirez", "Loana Barroso", "Pedro Thompson", "Alonso Jimenez", "Facundo Fernandez"] # Creamos la lista de estudiantes con las variables a utilizaar

            print (f"La lista actual es: {estudiantes}") # Imprimimos dicha lista

            pregunta = input ("¿Le gustaría agregar algun nombre o eliminarlo? Presione 1 para agregar, 2 para eliminar o 3 para no hacer nada ") # Pedimos un número a cambio de cada acción posible

            match pregunta: # Hacemos un match a cada número de respuesta
                case "1": # Opción agregar estudiante 
                    nombre = input ("Ingrese el nombre del estudiante que le gustaría agregar ") # Pedimos el estudiante a agregar
                    estudiantes.append (nombre) # Unimos ese estudiante a la lista previa
                case "2": # Opción eliminar estudiante 
                    eliminado = input ("Ingrese el nombre del estudiante que le gustaría eliminar ") # Pedimos el estudiante a eliminar
                    if eliminado in estudiantes: # Nos aseguramos de que se encuentre en la lista
                        estudiantes.remove (eliminado) # Usamos el método "Remove" para eliminarlo
                case "3":
                    break # Salimos del match
                case _: 
                    print ("Por favor ingrese un número del 1 al 3") # Por si no ponen el número correcto
            
            print (f"{estudiantes}") # Imprimimos la lista final

        case "6": # Ejerciciio 6
            lista = [41, 114, 141, 144, 414, 441, 14] # Creamos la lista a reordenar

            print (lista)            

            def bubble_sort (lista): # Elegi este método para practicar algo nuevo, fue díficil pensar una solución que cumpla la consigna
                n = len (lista)
                for i in range (n):
                    intercambio = False
                    for j in range (0, n - 1 -i):
                        if lista [j] > lista [j + 1]:
                            lista [j], lista [j + 1] = lista [j + 1], lista [j]
                            intercambio = True
                    if not intercambio:
                        break
            
            bubble_sort (lista)
            print (f"{lista}")

        case "7": # Ejercicio 7
            
            temperaturas = [ # Cargamos las temperaturas mínimas y máximas de 7 días
                [15,  20],
                [17, 19],
                [14, 20],
                [12, 21],
                [11, 22],
                [13, 23],
                [15, 24]
            ]
            
            temperaturas_minimas = 0 # Variable para la suma de temperaturas mínimas
            temperaturas_maximas = 0 # Variable para la suma de temperaturas maximas
            temperatura_minima = 0 # Variable para asignar la temperatura mínima de cada día
            temperatura_maxima = 0 # Variable para asignar la temperatura máxima de cada día

            t = len (temperaturas) # Calculamos la longitud de la lista "temperaturas"

            for h in range (t): # Hacemos un ciclo con la longitud de la lista "temperaturas"
                temperaturas_maximas += temperaturas [h] [1] # Para calcular las temperaturas máximas sumamos el índice en la lista de temperaturas que corresponden
                temperaturas_minimas += temperaturas [h] [0] # Para calcular las temperaturas mínimas sumamos el índice en la lista de temperaturas que corresponden 
            
                promedio_minimo = temperaturas_minimas / t # Calculamos el promedio de temperaturas mínimas con la suma previamente hecha dividida por la longitud de la lista
                promedio_maximo = temperaturas_maximas / t # Calculamos el promedio de temperaturas máximas con la suma previamente hecha dividida por la longitud de la lista

            print (f"Promedio de las temperaturas mínimas: {promedio_minimo:.2f}ºC, promedio de las temperaturas máximas: {promedio_maximo:.2f}ºC") # Imprimos los promedios redondeados a dos decimales

            amplitud = [] # Creamos la lista para registrar las amplitudes de cada día

            for k in range (t): # Hacemos un ciclo con la longitud de la lista "temperaturas"
                temperatura_maxima = temperaturas [k] [1] # Elegimos la temperatura máxima y mínima que corresponden al mismo día
                temperatura_minima = temperaturas [k] [0]
                amplitud.append (temperatura_maxima - temperatura_minima) # Creamos un resta para calcular la amplitud y la sumamos a la lista de amplitudes

            mayor = max(amplitud) # Calculamos el número de mayor amplitud
            dia = amplitud.index(mayor) # Calculamos el día que fue mas la amplitud gracias a saber previamente la mayor amplitud total

            print (f"El día con la mayor amplitud térmica fue el día {dia+1} con {mayor}ºC") # Imprimimos los resultados

        case "8":

            tabla = [[0]*4 for datos in range(6)] # Creamos una matriz de 4x6 celdas

            tabla[0][0] = "Estudiantes"  # Asignamos las variable inmoviles
            tabla[0][1] = "Programación"
            tabla[0][2] = "Matemática"
            tabla[0][3] = "AYSO"
            tabla[1][0] = "Santiago"
            tabla[2][0] = "Lucía"
            tabla[3][0] = "Facundo"
            tabla[4][0] = "Manuel"
            tabla[5][0] = "Ana"

            filascargar = 5   # Preparamos las variables que vamos a usar para los bucles 
            columnascargar = 4

            print("Ingrese los datos")

            for x in range(1, filascargar + 1): # Hacemos un bucle que empieza en 1 para no pisar los títulos
                print(f"Fila {x}") # Imprimimos un separador
                for i in range(1, columnascargar): # Hacemos un bucle anidado para las columnas
                    tabla[x][i] = int(input(f"Ingrese el valor posición {x},{i}:\n")) # Pedimos los valores de cada posicion a completar

            print("Tabla cargada:")
            for fila in tabla: # Imprimimos en un bucle cada fila de la tabla completa
                print(fila)

            for f in range (1, filascargar + 1): # Hacemos un bucle que empieza en 1 para no pisar los títulos
                for g in range (1, columnascargar): # Hacemos un bucle anidado para las columnas
                    promedioestudiantes = sum(tabla[f][1:]) # Sumamos en la variable cada nota de cada estudiante
                    promedioestudiantesfinal = promedioestudiantes / (columnascargar - 1) # restamos uno porque una columna tiene los nombres
                print (f"El promedio de {tabla[f][0]} es {promedioestudiantesfinal}") # Imprimimos el promedio de cada estudiante

            for h in range (1, columnascargar): # Hacemos un bucle que empieza en 1 para no pisar los títulos
                promediomaterias = 0
                for j in range(1, filascargar + 1): # Hacemos un bucle anidado para las columnas
                    promediomaterias += tabla [j][h] # Sumamos en la variable cada nota de cada materia
                    promediomateriasfinal = promediomaterias / filascargar
                print (f"El promedio de {tabla[0][h]} es {promediomateriasfinal}")

        case "9":

            contjugador = 0

            while contjugador <= 2:

                tateti = [["-"]*3 for datos in range(3)] # Creamos una matriz de 3x3 celdas

                print ("Tablero inicial: ")
                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                    print(fila)

                contjugador = 0

                while True:
                    contjugador = 0

                    for a in range (2):
                        contjugador += 1 

                        print (f"Turno del jugador {contjugador}")
                        turno = input ("Elija el espacio en donde quiere poner su ficha, separando fila de columna con una coma.Ejemplo: 1,3 (fila 1, columna 3)")
                        match turno:

                            case "1,1":
                                if contjugador == 1:
                                    del tateti [0] [0]
                                    tateti[0].insert (0, "X")
                                    
                                else:
                                    del tateti [0] [0]
                                    tateti[0].insert (0, "O")
                                    
                                
                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)
                                
                            case "1,2":
                                
                                if contjugador == 1:
                                    del tateti [0] [1]
                                    tateti[0].insert (1, "X")
                                else:
                                    del tateti [0] [1]
                                    tateti[0].insert (1, "O")

                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case "1,3":
                                
                                if contjugador == 1:
                                    del tateti [0] [2]
                                    tateti[0].insert (2, "X")
                                else:
                                    del tateti [0] [2]
                                    tateti[0].insert (2, "O") 

                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case "2,1":
                                
                                if contjugador == 1:
                                    del tateti [1] [0]
                                    tateti[1].insert (0, "X")
                                else:
                                    del tateti [1] [0]
                                    tateti[1].insert (0, "O")

                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case "2,2":

                                if contjugador == 1:
                                    del tateti [1] [1]
                                    tateti[1].insert (1, "X")
                                else:
                                    del tateti [1] [1]
                                    tateti[1].insert (1, "O") 
                                
                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)
                                
                            case "2,3":
                                
                                if contjugador == 1:
                                    del tateti [1] [2]
                                    tateti[1].insert (2, "X")
                                else:
                                    del tateti [1] [2]
                                    tateti[1].insert (2, "O")
                                
                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case "3,1":

                                if contjugador == 1:
                                    del tateti [2] [0]
                                    tateti[2].insert (0, "X")
                                else:
                                    del tateti [2] [0]
                                    tateti[2].insert (0, "O")
                                
                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case "3,2":
                                
                                if contjugador == 1:
                                    del tateti [2] [1]
                                    tateti[2].insert (1, "X")
                                else:
                                    del tateti [2] [1]
                                    tateti[2].insert (1, "O")
                                
                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case "3,3":
                                
                                if contjugador == 1:
                                    del tateti [2] [2]
                                    tateti[2].insert (2, "X")
                                else:
                                    del tateti [2] [2]
                                    tateti[2].insert (2, "O")
                                
                                print ("Tablero actual: ")
                                for fila in tateti: # Imprimimos en un bucle cada fila de la tabla completa
                                    print(fila)

                            case _: 
                                print ("No ingresó ninguna combinación válida, pierde el turno. ¡Más atención la próxima! ")
                                
                        if tateti [0][0] == "X" and tateti [0][1] == "X" and tateti [0][2] == "X":
                            print ("Felicidades, gana el jugador 1")
                            contjugador == 3
                            break

                        if tateti [0][0] == "O" and tateti [0][1] == "O" and tateti [0][2] == "O":
                            print ("Felicidades, gana el jugador 2")
                            break

                        if tateti [1][0] == "X" and tateti [1][1] == "X" and tateti [1][2] == "X":
                            print ("Felicidades, gana el jugador 1")
                            break

                        if tateti [1][0] == "O" and tateti [1][1] == "O" and tateti [1][2] == "O":
                            print ("Felicidades, gana el jugador 2")
                            break

                        if tateti [2] [0] == "X" and tateti [2][1] == "X" and tateti [2][2] == "X":
                            print ("Felicidades, gana el jugador 1")
                            break
                            
                        if tateti [2] [0] == "O" and tateti [2] [1] == "O" and tateti [2] [2] == "O":
                            print ("Felicidades, gana el jugador 2")
                            break
                            
                        if tateti [0] [2] == "X" and tateti [1][2] == "X" and tateti [2][2] == "X":
                            print ("Felicidades, gana el jugador 1")
                            break

                        if tateti [0] [2] == "O" and tateti [1] [2] == "O" and tateti [2] [2] == "O":
                            print ("Felicidades, gana el jugador 2")
                            break

                        if tateti [0] [0] == "X" and tateti [1] [1] == "X" and tateti [2][2] == "X":
                            print ("Felicidades, gana el jugador 1")
                            break

                        if tateti [0] [0] == "O" and tateti [1] [1] == "O" and tateti [2][2] == "O":
                            print ("Felicidades, gana el jugador 2")
                            break

                        if tateti [0] [2] == "X" and tateti [1] [1] == "X" and tateti [2][0] == "X":
                            print ("Felicidades, gana el jugador 1")
                            break

                        if tateti [0] [2] == "O" and tateti [1] [1] == "O" and tateti [2][0] == "O":
                            print ("Felicidades, gana el jugador 2")
                            break
                    
        case "10":

            productoscargar = 4   # Preparamos las variables que vamos a usar para los bucles 
            diascargar = 7

            precios = [[0]*diascargar for datos in range(productoscargar)] # Creamos una matriz de 4x7 celdas

            for x in range(productoscargar): # Hacemos un bucle 
                for i in range(diascargar): # Hacemos un bucle anidado para las columnas
                    precios[x][i] = int(input(f"Ingrese la ganancia {i+1} del producto {x+1}:\n")) # Pedimos los valores de cada posicion a completar

            print("Tabla cargada:")
            for fila in precios: # Imprimimos en un bucle cada fila de la tabla completa
                print(fila)
            
            contprod = 0
            sumaproductos = 0
            mayorventas =[]

            for z in range (productoscargar):
                sumaproductos = 0
                for k in range (diascargar):
                    contprod += 1
                    sumaproductos += precios [z] [k]
                
                mayorventas.append (sumaproductos)            
                print (f"La suma de la semanana para el producto {z+1} es de: {sumaproductos}")

            print (mayorventas)

            mayorventastotales = max(mayorventas) # Calculamos el número de mayores ventas
            diamayor = mayorventas.index(mayorventastotales) # Calculamos el día que fue las mayores ventas totales 
            print (f"El día con la mayores ventas fue el día {diamayor+1} con ${mayorventastotales} de ganancia") # Imprimimos los resultados
            
        case "11": 
            
            estudiantes10 = ["María Perez", "Juana Lopez", "Anabella Gutierrez", "Marisa Ramirez", "Loana Barroso", "Pedro Thompson", "Alonso Jimenez", "Facundo Fernandez", "Constanza Aparicio", "Luna Cabrera"]
        
            nombrebusqueda = input ("Ingrese el nombre que desea buscar ")
            if nombrebusqueda.isalpha:

                if nombrebusqueda.title() in estudiantes10:
                    print (f"{nombrebusqueda.title()} se encuentra en la lista de estudiantes")
                    indiceestudiante = estudiantes10.index(nombrebusqueda.title())
                    print (f"{nombrebusqueda.title()} se encuentra en el puesto {indiceestudiante+1} de la lista de Estudiantes")
                else:
                    print (f"{nombrebusqueda.title()} no se encuentra en la lista de estudiantes")
                
                
            else:
                print ("Ingrese solo letras en el nombre")

        case "12":

            lista8 = []

            for c in range (1,9):
                num = int(input (f"Ingrese el numero {c} "))
                if num == int(num):
                    lista8.append (num)
                else:
                    print ("Por favor ingrese un número")
            print(lista8)
            lista8.sort()
            print(lista8)
            lista8.reverse()
            print (lista8)

        case "13":

            puntajes = [450, 1200, 875, 990, 300, 1500, 640]

            puntajes.sort()

            print (f"El puntaje más bajo es el {puntajes[0]} y el puntaje más alto es el {puntajes[6]}")
            print ("Lista de puntajes: ")
            print (puntajes)

            indicepuntaje = puntajes.index(990)

            print (f"El puntaje 990 se encuentra en el puesto {indicepuntaje+1} en el ranking")

        case _:
            print ("Por favor ingrese un número del 1 al 13")