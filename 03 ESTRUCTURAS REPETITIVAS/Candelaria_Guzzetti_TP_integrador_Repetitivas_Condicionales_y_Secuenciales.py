# Trabajo realizado por Candelaria Guzzetti

while True: # Condicion para que se pueda repetir el selector de ejercicios una vez revisados

    ejercicio = input ("Introduzca el número de ejercicio del 1 al 5 ") 

    match ejercicio:
        case "1": # Ejercicio 1

            while True: 
                nombre = input("Ingrese el nombre del cliente, solo se permiten letras como caracteres. ") # Pedimos los datos del nombre
                if nombre.isalpha(): # Hacemos una condición para ver si los datos ingresados son caracteres de letras
                    print (f"Cliente: {nombre}") #Imprimimos los datos de ser letras
                    break
                else: # Condicion si los datos no son letras
                    print ("Por favor ingrese un nombre usando solo letras como caracteres.") # Imprimimos el aviso para que ingresen los datos correctos

            while True: 
                producto = input("Ingrese la cantidad de productos a comprar. ") # Pedimos los datos de la cantidad de productos 
                if producto.isdigit():
                    producto = int(producto) # Actualizamos el producto de string a integer para que pueda ser leido correctamente en la comparación de la condición
                    if producto > 0 : # Hacemos una condición para ver si el número ingresado es mayor a cero
                        cont_compra = 1 # Preparamos el contador, empieza en 1 para que diga correctamente el número de producto a pedir datos
                        precio_s_descuento = 0 # Preparamos la variable que va a guardar el precio final sin descuento
                        while cont_compra <= producto: # Comenzamos el bucle que va a estar activo solo para la cantidad de productos ingresados en el input "producto"
                            for x in range (producto): # Comenzamos el bucle anidado que va repetirse la cantidad de veces que diga el numero ingresado en el input "producto"
                                precio = input(f"¿Cual es el precio del producto {cont_compra}? ") # Entramos al bucle y pedimos el precio del producto que corresponde al contador de compra
                                if precio.isdigit(): # Validamos que sea un número el caracter ingresado
                                    precio = int(precio) # Volvemos integer el precio para poder hacer calculos
                                    precio_s_descuento += precio # Para calcular el precio sin descuento agregamos a la variable el valor del precio cada vez que se repite el bucle 
                                    descuento = input ("¿Tiene descuento? S para si, N para no. ") # Pedimos que nos digan si el producto tiene descuento, detallando las opciones de respuesta
                                    cont_compra += 1 # Actualizamos el contador asi en la próxima vuelta sigue diciendo el número correcto de producto ingresado
                                else: # Condicion si no es un dígito
                                    print ("Por favor ingrese un número.") # Imprimimos el aviso para que ingresen los datos correctos
                                    break # Salimos del bucle
                                
                                if descuento == "S" or descuento == "s": # Hacemos una condición para analizar los datos ingresados en el input "descuento".
                                    porcentaje = precio * 0.10 # Si usan las letras que corresponden a "si", calculamos el porcentaje de descuento que tiene el producto
                                    precio_c_descuento = precio - porcentaje # Calculamos el precio con descuento del producto restando el porcentaje de desciento al precio original
                                    ahorro = precio - precio_c_descuento # Calculamos la suma de precios
                                    ahorro += ahorro
                                elif descuento == "N" or descuento == "n": # Si usan las letras que corresponden a "no":...
                                    continue # ... Seguimos con el programa
                                else: # Si no usan ninguna de las letras pedidas: ...
                                    print ("Por favor ingrese S para si o N para no ") #... Aclaramos que ingresen los datos correctos
                                    break # Salimos del bucle
                        
                    precio_c_descuento_suma = precio_s_descuento - ahorro # Calculamos el total con descuentos
                    promedio = precio_c_descuento_suma / producto # Calculamos el promedio de los productos ingresados usando el precio con descuento dividido la cantidad de productos ingresada

                    print (f"Cliente: {nombre}") # Imprimimos el nombre del cliente
                    print (f"Cantidad de productos: {producto}") # Imprimimos la cantidad de productos ingresada
                    print (f"Total sin descuentos: {precio_s_descuento}") # Imprimimos el total de precio sin descuentos 
                    print (f"Total con descuentos:{precio_c_descuento_suma}") # Imprimimos el total de precio con descuentos 
                    print (f"Ahorro:{ahorro}") # Imprimimos el ahorro total
                    print (f"Promedio por producto:{promedio:.2f}") # Imprimimos el promedio de precio por producto sin contar el ahorro
                    break

                else:
                    print ("Ingrese un número mayor a cero")

        case "2": # Ejercicio 2

            usuario_correcto = "alumno" # Planteamos la variable de usuario que espereamos que escriban para continuar el programa
            clave_correcta = "python123" # Planteamos la variable de contraseña que espereamos que escriban para continuar el programa

            for j in range (1, 4): # Creamos un bucle que se repita 3 veces 
                usuario = input ("Ingrese su usuario ") # Pedimos el usuario correcto
                clave = input ("Ingrese su clave ") # Pedimos la clave correcta
                if usuario == usuario_correcto and clave == clave_correcta: 
                    print (f"Usuario: {usuario}") # Imprimimos el usuario que nos proporcionaron
                    print ("Acceso concedido.") # Les informamos que la combinación está correcta
                    break # Salimos del bucle 
                else: # Qué pasa si no se cumple la condición
                    print (f"Usuario: {usuario}") # Imprimimos el usuario que nos proporcionaron
                    print ("Error: credenciales inválidas.") # Si las credenciales no coinciden, imprimimos un aviso de error 

            if usuario == usuario_correcto and clave == clave_correcta: # Condición para saber si bloqueamos la cuenta luego del bucle
                pass # No hacemos nada y seguimos con el programa
            else: # Si la contraseña y clave no coinciden luego de 3 pases
                print ("Cuenta bloqueada") # Avisamos que se bloqueó la cuenta
                exit() #Terminamos el programa

            while True: #Planteamos el bucle 
                print ("Elija un número de las siguientes opciones:") # Imprimimos las opciones
                print ("1. Ver estado de inscripción") # Imprimimos las opciones
                print ("2. Cambiar clave") # Imprimimos las opciones
                print ("3. Mensaje motivacional") # Imprimimos las opciones
                print ("4. Salir") # Imprimimos las opciones
                opcion = input("Ingrese el número elegido ") # Pedimos elegir un número de la lista anterior
                if opcion.isdigit(): # Si ese número es un dígito...
                    match opcion: # ...  Lo unimos a una de las siguientes opciones
                        case "1": # Opcion "Ver el estado de inscripción"
                            print ("Usted está inscripto") # Imprime el resultado pedido
                        case "2": # Opción "Cambiar clave"
                            clave_nueva = input ("Ingrese su nueva clave, minimo 6 caracteres ") # Pedimos la nueva clave
                            if len(clave_nueva) >= 6: # Verificamos que la clave nueva tenga mínimo 6 dígitos
                                pass # Si es así, seguimos con el programa
                            else: # Si no tiene 6 o más dígitos...
                                print ("Error: mínimo 6 caracteres.") # Imprimimos el error
                                continue # Volvemos al menú
                            clave_confirmacion = input ("Confirme su nueva clave ") #  Si ya verificamos que la contraseña tenga 6 o más dígitos, pedimos la confirmación de la misma
                            if clave_nueva == clave_confirmacion: # Verificamos que ambas contrseñas ingresadas sean iguales
                                print ("Contraseña cambiada exitosamente") # Avisamos que se logró el cambio
                                clave_correcta = clave_nueva # Actualizamos la clave
                            else: # Si las claves no son iguales...
                                print ("Error: Las claves no coinciden.") # Imprimimos el aviso por pantalla
                        case "3": # Opción "Mensaje motivacional"
                            print ("La paciencia es el don de la ciencia, ¡No te rindas! Vas a poder con todo.") # Frase muy motivacional
                        case "4": # Opción "Salir"
                            print ("¡Adios!") # Saludamos
                            exit()
                        case _: # Opción si no ingresan un número del 1 al 4
                            print ("Ingrese un número del 1 al 4 para poder continuar.") # Avisamos lo que tienen que hacer 
                else: # Si el caracter ingresado no es un número...
                    print ("Ingrese un número del 1 al 4 para poder continuar.") # Pedimos que ingresen un número para poder seguir con el programa

        case "3": # Ejercicio 3

            while True:
                nombre = input ("Ingrese el nombre del operador ")
                if nombre.isalpha():
                    break
                else:
                    print ("Ingrese solo letras como caracteres")

            lunes1 = " "
            lunes2 = " "
            lunes3 = " "
            lunes4 = " "
            martes1 = " "
            martes2 = " "
            martes3 = " "

            while True:
                print ("Elija una opción de las siguientes:")
                print ("1. Reservar turno")
                print ("2. Cancelar turno (por nombre)")
                print ("3. Ver agenda del día")
                print ("4. Ver resumen general")
                print ("5. Cerrar sistema")
                opcion = input ("Ingrese el número de la opción elegida ")
                if opcion.isdigit():
                    match opcion:
                        case "1":
                            dia = int(input("Ingrese el día a reservar: Lunes (1) o Martes (2) "))
                            match dia:
                                case 1:
                                    paciente = input ("Ingrese el nombre del paciente ")
                                    if paciente.isalpha(): 
                                        if paciente == lunes1:
                                            print ("El paciente ya está agendado en el 1er horario del lunes")
                                        elif paciente == lunes2:
                                            print ("El paciente ya está en el 2do horario del lunes")
                                        elif paciente == lunes3:
                                            print ("El paciente ya está agendando en le 3er horario del lunes")
                                        elif paciente == lunes4:
                                            print ("El paciente ya está agendado en el 4to horario del lunes")
                                        if lunes1 == " " and paciente != lunes2 and paciente != lunes3 and paciente != lunes4:
                                            lunes1 = paciente
                                            print ("Paciente agendado en el 1er horario del lunes")
                                        elif lunes2 == " " and paciente != lunes1 and paciente != lunes3 and paciente != lunes4:
                                            lunes2 = paciente
                                            print ("Paciente agendado en el 2do horario del lunes")
                                        elif lunes3 == " " and paciente != lunes2 and paciente != lunes4 and paciente != lunes1:
                                            lunes3 = paciente
                                            print ("Paciente agendado en el 3er horario del lunes")  
                                        elif lunes4 == " "and paciente != lunes2 and paciente != lunes3 and paciente != lunes1:
                                            lunes4 = paciente
                                            print ("Paciente agendado en el 4to horario del lunes")
                                        else:
                                            if paciente != lunes1 and paciente != lunes2 and paciente != lunes3 and paciente != lunes4:
                                                print ("No hay horarios disponibles el lunes")
                                            else:
                                                continue
                                    else:
                                        print ("Por favor ingrese solo letras como caracteres")
                                case 2:
                                    paciente = input ("Ingrese el nombre del paciente ")
                                    if paciente.isalpha(): 
                                        if paciente == martes1:
                                            print ("El paciente ya está agendado en el 1er horario del martes")
                                        elif paciente == martes2:
                                            print ("El paciente ya está en el 2do horario del martes")
                                        elif paciente == martes3:
                                            print ("El paciente ya está agendando en le 3er horario del martes")
                                        if martes1 == " " and paciente != martes2 and paciente != martes3:
                                            martes1 = paciente
                                            print ("Paciente agendado en el 1er horario del martes")
                                        elif martes2 == " " and paciente != martes1 and paciente != martes3:
                                            martes2 = paciente
                                            print ("Paciente agendado en el 2do horario del martes")
                                        elif martes3 == " " and paciente != martes2 and paciente != martes1:
                                            martes3 = paciente
                                            print ("Paciente agendado en el 3er horario del martes")  
                                        else:
                                            if paciente != martes1 and paciente != martes2 and paciente !=  martes3:
                                                print ("No hay horarios disponibles el martes")
                                            else:
                                                continue
                                    else:
                                        print ("Por favor ingrese solo letras como caracteres")
                        case "2":
                            dia = int(input("Ingrese el día a cancelar: Lunes (1) o Martes (2) "))
                            match dia:
                                case 1:
                                    paciente = input ("Ingrese el nombre del paciente ")
                                    if paciente.isalpha():
                                        if paciente == lunes1:
                                            lunes1 = " "
                                            print ("Turno en el 1er horario cancelado")
                                        elif paciente == lunes2:
                                            lunes2 = " "
                                            print ("Turno en el 2do horario cancelado")
                                        elif paciente == lunes3:
                                            lunes3 = " "
                                            print ("Turno en el 3er horario cancelado")
                                        elif paciente == lunes4:
                                            lunes4 = " "
                                            print ("Turno en el 3er horario cancelado")
                                        else:
                                            print ("No hay turnos asignados para ese paciente el día lunes")
                                case 2:
                                    paciente = input ("Ingrese el nombre del paciente ")
                                    if paciente.isalpha():
                                        if paciente == martes1:
                                            martes1 = " "
                                            print ("Turno en el 1er horario cancelado")
                                        elif paciente == martes2:
                                            martes2 = " "
                                            print ("Turno en el 2do horario cancelado")
                                        elif paciente == martes3:
                                            martes3 = " "
                                            print ("Turno en el 3er horario cancelado")
                                        else:
                                            print ("No hay turnos asignados para ese paciente el día martes")
                                case _:
                                    print ("Por favor ingrese 1 para lunes o 2 para martes")
                        case "3":
                            dia = int(input("Ingrese el día a reservar: Lunes (1) o Martes (2) "))
                            match dia:
                                case 1:
                                    print ("Los turnos disponibles son los siguientes:")
                                    if lunes1 == " ":
                                        print ("Turno 1 del lunes: libre")
                                    else:
                                        print ("Turno 1 del lunes: ocupado")
                                    if lunes2 == " ":
                                        print ("Turno 2 del lunes: libre")
                                    else:
                                        print ("Turno 2 del lunes: ocupado")
                                    if lunes3 == " ":
                                        print ("Turno 3 del lunes: libre")
                                    else:
                                        print ("Turno 3 del lunes: ocupado")
                                    if lunes4 == " ":
                                        print ("Turno 4 del lunes: libre")
                                    else:
                                        print ("Turno 4 del lunes: ocupado")
                                case 2:
                                    print ("Los turnos disponibles son los siguientes:")
                                    if martes1 == " ":
                                        print ("Turno 1 del martes: libre")
                                    else:
                                        print ("Turno 1 del martes: ocupado")
                                    if martes2 == " ":
                                        print ("Turno 2 del martes: libre")
                                    else:
                                        print ("Turno 2 del martes: ocupado")
                                    if martes3 == " ":
                                        print ("Turno 3 del martes: libre")
                                    else:
                                        print ("Turno 3 del martes: ocupado")
                                case _:
                                    print ("Por favor ingrese 1 para lunes o 2 para martes")
                        case "4":
                            print ("Los turnos son los siguientes:")
                            if lunes1 == " ":
                                print ("Turno 1 del lunes: libre")
                            else:
                                print ("Turno 1 del lunes: ocupado")
                            if lunes2 == " ":
                                print ("Turno 2 del lunes: libre")
                            else:
                                print ("Turno 2 del lunes: ocupado")
                            if lunes3 == " ":
                                print ("Turno 3 del lunes: libre")
                            else:
                                print ("Turno 3 del lunes: ocupado")
                            if lunes4 == " ":
                                print ("Turno 4 del lunes: libre")
                            else:
                                print ("Turno 4 del lunes: ocupado")
                            if martes1 == " ":
                                print ("Turno 1 del martes: libre")
                            else:
                                print ("Turno 1 del martes: ocupado")
                            if martes2 == " ":
                                print ("Turno 2 del martes: libre")
                            else:
                                print ("Turno 2 del martes: ocupado")
                            if martes3 == " ":
                                print ("Turno 3 del martes: libre")
                            else:
                                print ("Turno 3 del martes: ocupado")
                            cont_lunes = 0
                            cont_martes = 0
                            if lunes1 != " ":
                                cont_lunes += 1
                            else:
                                pass
                            if lunes2 != " ":
                                cont_lunes += 1
                            else:
                                pass
                            if lunes3 != " ":
                                cont_lunes += 1
                            else:
                                pass
                            if lunes4 != " ":
                                cont_lunes += 1
                            else:
                                pass
                            if martes1 != " ":
                                cont_martes += 1
                            else:
                                pass
                            if martes2 != " ":
                                cont_martes += 1
                            else:
                                pass
                            if martes3 != " ":
                                cont_martes += 1
                            else:
                                pass
                            if cont_lunes > cont_martes:
                                print (f"El día con más turnos asignados es el lunes (Turnos:{cont_lunes})")
                            elif cont_lunes < cont_martes:
                                print (f"El día con más turnos asignados es el martes (Turnos:{cont_martes})")
                            else:
                                print (f"Hay la misma cantidad de turnos asignados los dos días (Turnos:{cont_lunes})")
                        case "5":
                            print ("¡Adios!") # Saludamos
                            exit()
                        case _:
                            print ("Por favor ingrese una opción del 1 al 5")
                else:
                    print ("Ingrese un número del 1 al 5")

        case "4": # Ejercicio 4


            energia = 100
            tiempo = 12
            cerraduras_abiertas = 0
            alarma = False
            codigo_parcial = ""
            cont_forzar = 0
            cont_hackear = 0
            cont_descansar = 0
            cont_codigo = 0


            while True:
                    nombre = input ("Ingrese el nombre del agente ")
                    while nombre.isalpha():
                        print (f"Agente activo: {nombre}")
                        print (f"Energía: {energia}")
                        print (f"Tiempo: {tiempo} minutos")
                        print (f"Cerraduras Abiertas: {cerraduras_abiertas}")
                        print ("1. Forzar cerradura")
                        print ("2. Hackear panel")
                        print ("3. Descansar")
                        opcion = input("Elija una opción del 1 al 3 ")
                        while opcion.isdigit():
                            match opcion:
                                case "1":
                                    if energia < 40 and alarma == False:
                                        print ("Hay riesgo de alarma")
                                    energia = energia - 20
                                    tiempo = tiempo - 2
                                    cont_forzar += 1
                                    riesgo = input ("Elija un número del 1 al 3 para evitar la alarma ")
                                    while riesgo.isdigit():
                                        if riesgo == "1" or riesgo == "2" or riesgo == "3":
                                            continue
                                        else:
                                            print ("Por favor ingrese un número del 1 al 3")
                                            break
                                    riesgo = int(riesgo)
                                    if riesgo == 3 and cerraduras_abiertas <= 2:
                                        alarma = True
                                        print ("Empieza a sonar la alarma")
                                        print ("No logra abrir la cerradura")
                                        break
                                    elif (riesgo == 1 or riesgo == 2) and cerraduras_abiertas <= 1:
                                        print ("Logra abrir 1 cerradura")
                                        cerraduras_abiertas += 1
                                        break
                                    elif (riesgo == 1 or riesgo == 2) and cerraduras_abiertas == 2: 
                                        if cont_forzar == 3 and (cont_hackear == 0 and cont_descansar == 0):
                                            if alarma == True:
                                                print ("Con la alarma sonando, se traba la cerradura debido a sus recurrentes intentos de abrirla ")
                                            else:                        
                                                print ("Empieza a sonar la alarma debido a sus recurrentes intentos de abrir la cerradura ")
                                                print ("No logra abrir la cerradura")
                                                cont_forzar = 0
                                                cont_hackear = 0
                                                cont_descansar = 0
                                                break
                                    if cont_hackear < 3 and (cont_hackear > 0 or cont_descansar > 0):
                                            cont_forzar = 0
                                            cont_hackear = 0
                                            cont_descansar = 0
                                            break
                                case "2":
                                        energia = energia - 10
                                        tiempo = tiempo - 3
                                        cont_hackear +=1 
                                        if cerraduras_abiertas <= 2:
                                            if cont_codigo >= 0 and cont_codigo <= 4:
                                                for x in range (1,5):
                                                    cont_codigo +=1
                                                    if cont_codigo == 1:
                                                        codigo_parcial += "M"
                                                        print (f"Código: {codigo_parcial}")
                                                    elif cont_codigo == 2:
                                                        codigo_parcial += "A"
                                                        print (f"Código: {codigo_parcial}")
                                                    elif cont_codigo == 3:
                                                        codigo_parcial += "U"
                                                        print (f"Código: {codigo_parcial}")
                                                    elif cont_codigo == 4:
                                                        codigo_parcial += "L"
                                                        print (f"Código: {codigo_parcial}")
                                                cont_codigo += 1
                                                if len(codigo_parcial) <= 8:
                                                    cerraduras_abiertas += 1
                                                    print ("Has abierto una cerradura")
                                                break
                                            if cont_codigo > 4 and cont_codigo <= 8:  
                                                for x in range (1,5):
                                                    cont_codigo +=1
                                                    if cont_codigo == 5:
                                                        codigo_parcial += "L"
                                                        print (f"Código: {codigo_parcial}")
                                                    elif cont_codigo == 6:
                                                        codigo_parcial += "I"
                                                        print (f"Código: {codigo_parcial}")
                                                    elif cont_codigo == 7:
                                                        codigo_parcial += "D"
                                                        print (f"Código: {codigo_parcial}")
                                                    elif cont_codigo == 8:
                                                        codigo_parcial += "O"
                                                        print (f"Código: {codigo_parcial}")
                                                        print ("Código completo")
                                            if len(codigo_parcial) <= 8 and  len(codigo_parcial) >=5:
                                                cerraduras_abiertas += 1
                                                print ("Has abierto una cerradura")
                                                break
                                        else:
                                            print ("Ya abrió todas las cerraduras posibles usando este método")
                                            break
                                case "3":
                                    if energia < 100:
                                        energia += 15
                                    tiempo -= 1
                                    if alarma == True:
                                        energia -= 10
                                    print ("Se toma un breve descanso")
                                    break
                                case _:
                                    print ("Por favor ingrese un número del 1 al 3")
                                    break
                        else:
                            print ("Elija un número del 1 al 3")
                        if alarma == True and tiempo <= 3:
                            print ("DERROTA (bloqueo)")
                            break
                        elif cerraduras_abiertas == 3:
                            print ("VICTORIA")
                            break
                        elif energia <= 0 or tiempo <= 0:
                            print ("DERROTA")
                            break
                    else:
                        print ("Por favor ingrese solo letras como caracteres")
                    

        case "5": # Ejercicio 5

            vida_gladiador = 100 
            vida_enemigo = 100
            pociones_vida = 3
            danio_base_ataque_pesado = 15 
            danio_base_enemigo = 12
            turno_gladiador = True

            while True:
                nombre = input ("Ingrese el nombre del gladiador ")
                while nombre.isalpha():
                    print (f"Vida enemigo: {vida_enemigo}")
                    print (f"Vida gladiador: {vida_gladiador}")
                    print ("Las opciones son las siguentes:")
                    print ("1. Ataque pesado")
                    print ("2. Ráfaga Veloz")
                    print ("3. Curar")
                    opcion = input ("Ingrese el número de la acción que quiere realizar ")
                    if opcion.isdigit():
                        match opcion:
                            case "1":
                                    if vida_enemigo >= 20:
                                        vida_enemigo -= danio_base_ataque_pesado
                                        print(f"¡Atacaste al enemigo por {danio_base_ataque_pesado} puntos de daño!")
                                    else:
                                        danio_critico = danio_base_ataque_pesado * 1.5
                                        vida_enemigo -= danio_critico
                                        print(f"¡Atacaste al enemigo por {danio_critico} puntos de daño!")
                            case "2":
                                for x in range (1, 4):
                                    vida_enemigo -= 5
                                    print ("Golpe conectado por 5 de daño")
                            case "3":
                                if pociones_vida > 0:
                                    vida_gladiador += 30
                                    pociones_vida -= 1
                                else:
                                    print ("¡No quedan pociones!")
                                    break
                    else:
                        print ("Elija un número del 1 al 3")
                    vida_gladiador -= 12
                    print ("¡El enemigo te atacó por 12 puntos de daño!")
                    if vida_gladiador > 0 and vida_enemigo <= 0:
                        print (f"¡VICTORIA! {nombre} ha ganado la batalla.")
                        break
                    elif vida_gladiador <= 0:
                        print ("DERROTA. Has caído en combate.")
                        break
                else:
                    print ("Por favor ingrese solo letras como caracteres")
        
        case _: 
            print ("Por favor ingrese un número del 1 al 5")