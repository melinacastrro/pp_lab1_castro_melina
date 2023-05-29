import json
import re
import csv

def leer_archivo(archivo_json:str)->list:
    '''
    Abre un archivo json en modo lectura
    Recibe un archivo json
    Retorna una lista
    '''
    lista_jugadores = []
    with open(archivo_json,'r') as archivo:
        diccionario_jugadores = json.load(archivo)
        lista_jugadores = diccionario_jugadores['jugadores']
        return lista_jugadores
    
lista_jugadores = leer_archivo(r'C:\Users\54113\OneDrive\Escritorio\Guia de ejercicios\parcial.py\dt.json')



def mostrar_nombre_posicion(lista_jugadores:list)-> None:
    '''
    Itera la lista para obtener los elementos
    Recibe una lista
    '''
    for jugador in lista_jugadores:
        print("{0} | {1}".format(jugador["nombre"],jugador["posicion"]))


def mostrar_estadisticas(lista_jugadores: list):
    '''
    Crea una lista de datos y la exporta a un archivo csv
    Recibe una lista
    '''
    lista_datos = []
    cantidad = len(lista_jugadores)
    indice = input("Ingrese el indice del jugador a buscar: ")
    indice_int = int(indice)
    if indice_int >= 0 and indice_int < cantidad:
        jugador = lista_jugadores[indice_int]
        estadisticas = jugador["estadisticas"]
        for clave, value in estadisticas.items():
            clave_valida = re.sub("_", " ", clave)
            dato = "{0} : {1}".format(clave_valida, value)
            print(dato)
            lista_datos.append(dato)
        nombre_archivo = r"C:\Users\54113\OneDrive\Escritorio\repo parcial\repo_parcial\archivo.csv"
        with open(nombre_archivo, "w") as file:
            file.write(jugador["nombre"] + "\n")
            file.write(jugador["posicion"] + "\n")
            for dato in lista_datos:
                file.write(str(dato) + "\n")
    else:
        print("El índice ingresado no es válido.")


def calcular_promedio(lista_jugadores:list)->list:
    '''
    Calcula el promedio de puntos por partido
    Recibe una lista
    Retorna el promedio del dato buscado en la lista
    '''
    acumulador = 0
    contador = 0
    for jugador in lista_jugadores:
        acumulador += jugador["estadisticas"]["promedio_puntos_por_partido"]
        contador +=1
    if contador > 0 :
        promedio = acumulador/contador
    else:
        return "Error"     
        
    
    return promedio


def mostrar_promedio(lista_jugadores: list)->list:
    '''
    Crea una lista de promedios y los muestra 
    Recibe una lista
    Retorna una lista nueva con el promedio buscado
    '''
    promedios_puntos = []
    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        promedios_punto = jugador["estadisticas"]["promedio_puntos_por_partido"]
        nombre_y_promedio= ("{0}:{1}".format(nombre,promedios_punto))
        promedios_puntos.append(nombre_y_promedio)

    return promedios_puntos




def calcular_y_mostrar_max_jugador(lista_jugadores:list, clave:str)->None:
    '''
    Calcula y muestra el maximo valor de una clave en la lista
    Recibe un lista
    '''
    maximo = 0
    jugador_maximo = None


    for jugador in lista_jugadores:
        if "estadisticas" in jugador and clave in jugador["estadisticas"]:
            valor = jugador["estadisticas"][clave]
            if valor > maximo:
                maximo = valor
                jugador_maximo = jugador["nombre"]
    
    if jugador_maximo:
        clave_validada = re.sub("_"," ",clave)
        print("{0} | {1}:{2}".format(jugador_maximo,clave_validada,maximo))
    
    
     



def mostrar_logros(lista_jugadores:list)->list:
    '''
    Busca un jugador por su nombre, lo agrega a lista y muestra sus logros
    Recibe una lista
    Retorna una lista
    '''
    nombre = input("Ingrese el nombre del jugador: ")
    patron = " "
    if re.match(r"^[A-Za-z]{3}", nombre):
        patron = nombre
    else:
        return "No se encontró ningún jugador."

    logros_encontrados = []
    for jugador in lista_jugadores:
        if patron.lower() in jugador["nombre"].lower():
            logros_encontrados.append(jugador["logros"])

    if logros_encontrados:
        return logros_encontrados
    else:
        return "No se encontró ningún jugador con el nombre proporcionado."


def verificar_salon_fama(lista_jugadores:list):
    '''
    Verifica si el nombre del jugador ingresado se encuentra en el salon de la fama
    Recibe una lista
    Retorna true en caso de encontrarlo o false si no lo encuentra
    
    '''
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        logros = jugador["logros"]
        if nombre_jugador.lower() == nombre.lower() and "Miembro del Salon de la Fama del Baloncesto" in logros:
            return True
    return False

                     
def ivan_sort_A(lista_original:list)->list:
    '''
    Ordena una lista de manera ascendente
    Recine una lista
    Retorna una lista ordenada
    '''
    lista = lista_original[:]
    rango_a = len(lista)
    flag_swap = True
    contador = 0
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            contador += 1
            if  lista[indice_A] > lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True

    
    return lista

      
def calcula_jugadores_mayor_promedio(lista_jugadores:list, clave:str,valor:float):
    '''
    Calcula los jugadores con mayor promedio y los añade a una lista
    Recibe una lista, una clave y un valor numerico
    Retorna una lista de los jugadores seleccionados
    '''
    

    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        estadisticas = jugador["estadisticas"]
        if clave in estadisticas:
            promedio = estadisticas[clave]
        if promedio > valor:
            jugadores_seleccionados.append(jugador)

    return jugadores_seleccionados

def mostrar_jugadores_mayor_al_promedio(lista_jugadores:list, clave:str):
    '''
    Muestra los jugadores con mayor promedio del nivel ingresado
    Recibe una lista y la clave a calcular
    '''
    valor = input("Ingrese un valor numerico: ")
    valor_float = float(valor)


    jugadores_mayor_promedio = calcula_jugadores_mayor_promedio(lista_jugadores,clave,valor_float)
    
    if jugadores_mayor_promedio:
        for jugador in jugadores_mayor_promedio:
            nombre = jugador["nombre"]
            promedio = jugador["estadisticas"][clave]
            print("Jugador: {0}".format(nombre))
            clave_sin_guion = re.sub("_"," ",clave)
            print("Promedio de {0} por partido: {1}".format(clave_sin_guion, promedio))
            
    else:
        print("No se encontraron jugadores con promedio de {0} mayor que {1}.".format(clave, valor))

def obtener_jugador_mayor_logros(lista_jugadores:list)->str:
    '''
    Obtiene el jugador con mayores logros de la lista
    Recibe una lista
    Retorna un mensaje
    '''
    jugador_mayor_logros = None
    max_logros = 0

    for jugador in lista_jugadores:
        logros = len(jugador["logros"])
        if logros > max_logros:
            max_logros = logros
            jugador_mayor_logros = jugador["nombre"]
            mensaje = "El jugador con mas logros es {0}:{1}".format(jugador_mayor_logros,max_logros)

    return mensaje

def crear_lista_de_promedio(lista_jugadores:list)->list:
    '''
    Crea una lista con los promedios de puntos por partido ordenados de manera ascendente
    Recibe una lista
    Retorna una lista ordenada
    '''
    promedios_puntos = []
    for jugador in lista_jugadores:
        total_promedios_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios_puntos.append(total_promedios_puntos)

    promedios_puntos_ordenado = ivan_sort_A(promedios_puntos)

    return promedios_puntos_ordenado

def promedio_sin_menor(lista_jugadores:list)->float:
    '''
    Calcula el promedio total excluyendo al menor valor de la lista previamente ordenada
    Recibe una lista
    Retorna un resultado
    '''
    lista_promedios = crear_lista_de_promedio(lista_jugadores)
    suma_promedios = 0
    cantidad = len(lista_promedios) - 1
    for promedio in lista_promedios[1:]:
        suma_promedios += promedio
        resultado = suma_promedios/cantidad


    return resultado

def buscar_jugadores_con_porcentaje_superior(lista_jugadores:list, porcentaje:float)->list:
    '''
    Filtra jugadores que son mayores al porcentaje
    Recibe una lista y un valor flotante
    Retorna una lista con los valores ordenados
    '''
    jugadores_filtrados = []

    for jugador in lista_jugadores:
        porcentaje_tiros_de_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if porcentaje_tiros_de_campo > porcentaje:
            jugadores_filtrados.append(jugador)  

    return jugadores_filtrados

def mostrar_jugadores_con_porcentaje_superior(lista_jugadores:list):  
    '''
    Muestra los jugadores con mayor porcentaje que el valor ingresado
    Recibe una lista
    Retorna una lista ordenada
    '''    
    porcentaje = input("Ingrese un valor numerico: ")
    porcentaje_float = float(porcentaje)

    jugadores_filtrados = buscar_jugadores_con_porcentaje_superior(lista_jugadores,porcentaje_float)
    
    if jugadores_filtrados:
        for jugador in jugadores_filtrados:
            nombre = jugador["nombre"]
            posicion = jugador["posicion"]
            promedio = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
            print("Jugador: {0}".format(nombre))
            print("Posicion: {0}".format(posicion))
            print("Promedio de  {0}".format( promedio))
    else:
        print("No se encontraron jugadores con promedio  mayor que {0}.".format(promedio))

    jugadores_filtrados_ordenados = ivan_sort_A(jugadores_filtrados)

    return jugadores_filtrados_ordenados    


def menu():
    menu = "1 - Mostrar todos los jugadores del Dream Team\n"\
    "2 - Mostrar estadísticas de un jugador\n"\
    "3 - Buscar un jugador por su nombre y mostrar sus logros\n"\
    "4 - Mostrar promedio de puntos por partido de todo el Dream Team\n"\
    "5 - Mostrar si es Miembro del Salón de la Fama del Baloncesto\n"\
    "6 - Jugador con la mayor cantidad de rebotes totales\n"\
    "7 - Jugador con el mayor porcentaje de tiros de campo\n"\
    "8 - Jugador con la mayor cantidad de asistencias totales\n"\
    "9 - Mostrar los jugadores que han promediado más puntos por partido que el valor ingresado\n"\
    "10 - Mostrar los jugadores que han promediado más rebotes por partido que el valor ingresado\n"\
    "11 - Mostrar los jugadores que han promediado más asistencias por partido que el valor ingresado\n"\
    "12 - Jugador con la mayor cantidad de robos totales\n"\
    "13 - Jugador con la mayor cantidad de bloqueos totales\n"\
    "14 - Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior al valor ingresado\n"\
    "15 - Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\n"\
    "16 - Jugador con la mayor cantidad de logros obtenidos\n"\
    "17 - Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior al valor ingresado\n"\
    "18 - Jugador con la mayor cantidad de temporadas jugadas\n"\
    "19 - Mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior al valor ingresado\n"\
    "20 - BONUS !!! Mostrar la posición de cada jugador en los siguientes rankings:Puntos, Rebotes, Asistencias y Robos\n"\
    "0 - SALIR\n"

    
    return menu
    
def validar_entero(string:str):
    if type (string) == str:
        return int(string)
    else:
        return -1
    
def opcion_elegida():
    opcion = validar_entero(input(menu()))
    if opcion:
        return opcion
    else:
        return -1

def menu_final(lista_jugadores):
    match(opcion_elegida()):
        case 1:
            mostrar_nombre_posicion(lista_jugadores)
        case 2:
            mostrar_nombre_posicion(lista_jugadores)
            mostrar_estadisticas(lista_jugadores)
        case 3:
            print(mostrar_logros(lista_jugadores))
        case 4:
            print("El promedio total de puntos por partidos del dream team es : {0}".format(calcular_promedio(lista_jugadores)))
            for promedios in ivan_sort_A(mostrar_promedio(lista_jugadores)):
                print(promedios)
        case 5:
            if verificar_salon_fama(lista_jugadores):
                print("El jugador es miembro del salon de la fama")
            else:
                print("El jugador no es miembro del salon de la fama")    
        case 6:
            calcular_y_mostrar_max_jugador(lista_jugadores, "rebotes_totales")
        case 7:
            calcular_y_mostrar_max_jugador(lista_jugadores, "porcentaje_tiros_de_campo")
        case 8:
            calcular_y_mostrar_max_jugador(lista_jugadores, "asistencias_totales")
        case 9:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"promedio_puntos_por_partido")
        case 10:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"promedio_rebotes_por_partido")
        case 11:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"asistencias_totales")
        case 12:
            calcular_y_mostrar_max_jugador(lista_jugadores,"robos_totales")
        case 13:
            calcular_y_mostrar_max_jugador(lista_jugadores,"bloqueos_totales")
        case 14:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"porcentaje_tiros_libres")
        case 15:
            print("El promedio de dream team sin el menor promedio es : {0}".format(promedio_sin_menor(lista_jugadores)))
        case 16:
            print(obtener_jugador_mayor_logros(lista_jugadores))
        case 17:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"porcentaje_tiros_triples")
        case 18:
            calcular_y_mostrar_max_jugador(lista_jugadores,"temporadas")
        case 19:
            mostrar_jugadores_con_porcentaje_superior(lista_jugadores)
        case 23:
            pass
        case _:
            pass

while True :
    menu_final(lista_jugadores)
