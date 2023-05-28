import json
import re
import csv

def leer_archivo(archivo_json:str)->list:
    lista_jugadores = []
    with open(archivo_json,'r') as archivo:
        diccionario_jugadores = json.load(archivo)
        lista_jugadores = diccionario_jugadores['jugadores']
        return lista_jugadores
    
lista_jugadores = leer_archivo(r'C:\Users\54113\OneDrive\Escritorio\Guia de ejercicios\parcial.py\dt.json')



def mostrar_nombre_posicion(lista_jugadores):
    lista_datos = []
    for indice in lista_jugadores:
        nombre = indice["nombre"]
        posicion = indice["posicion"]
        nombre_posicion = ("{0}|{1}".format(nombre,posicion))
        lista_datos.append(nombre_posicion)

    return lista_datos


def mostrar_estadisticas(lista_jugadores: list):
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




      
    
        

#   
         
def calcular_promedio(lista_jugadores):
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


def crear_diccionario(lista_jugadores: list):
    promedios_puntos = []
    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        promedios_punto = jugador["estadisticas"]["promedio_puntos_por_partido"]
        nombre_y_promedio= ("{0}:{1}".format(nombre,promedios_punto))
        promedios_puntos.append(nombre_y_promedio)


    
    
    return promedios_puntos




def calcular_y_mostrar_max_jugador(lista_jugadores, clave):
    maximo = 0
    jugador_maximo = None


    for jugador in lista_jugadores:
        if "estadisticas" in jugador and clave in jugador["estadisticas"]:
            valor = jugador["estadisticas"][clave]
            if valor > maximo:
                maximo = valor
                jugador_maximo = jugador["nombre"]
    
    if jugador_maximo:
        print("{0} | {1}:{2}".format(jugador_maximo,clave,maximo))
    
    
     




def mayor_al_valor_ingresado(lista_jugadores, valor_ingresado:int,clave):
    
    contador_jugadores = 0
    valor_ingresado = input("Ingrese el valor numerico a buscar: ")
    for jugador in lista_jugadores:
        if valor_ingresado in jugador and clave in jugador["estadisticas"]:
            if valor_ingresado > jugador[clave]:
                contador_jugadores += clave["nombre"]

    return contador_jugadores


def mostrar_logros(lista_jugadores):
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


def miembro_del_salon_de_la_fama (lista_jugadores):
    nombre = input("ingrese el nombre del jugador: ")
    patron = " "
    if re.match(r"^[A-Za-z]{3}", nombre):
        patron = nombre
    else:
        return "No se encontró ningún jugador."
    
    salon_de_la_fama = []
    for jugador in lista_jugadores:
        clave = jugador["logros"]["Miembro del Salon de la Fama del Baloncesto"]
        if "logros" in jugador and clave in jugador["logros"]:

            if patron.lower() in jugador["nombre"].lower():
                salon_de_la_fama.append(jugador["nombre"])  
    if salon_de_la_fama:
        return salon_de_la_fama
    else:
        return "No se encontro"

                     
def ivan_sort_A(lista_original:list):
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

      
def mostrar_jugadores_mayor_promedio(lista_jugadores, clave,valor):
    

    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        estadisticas = jugador["estadisticas"]
        if clave in estadisticas:
            promedio = estadisticas[clave]
        if promedio > valor:
            jugadores_seleccionados.append(jugador)

    return jugadores_seleccionados

def mostrar_jugadores_mayor_al_promedio(lista_jugadores, clave):
    valor = input("Ingrese un valor numerico: ")
    valor_float = float(valor)

    jugadores_mayor_promedio = mostrar_jugadores_mayor_promedio(lista_jugadores,clave,valor_float)
    
    if jugadores_mayor_promedio:
        for jugador in jugadores_mayor_promedio:
            nombre = jugador["nombre"]
            promedio = jugador["estadisticas"][clave]
            print("Jugador: {0}".format(nombre))
            print("Promedio de {0} por partido: {1}".format(clave, promedio))
            print("-" * 30)
    else:
        print("No se encontraron jugadores con promedio de {0} mayor que {1}.".format(clave, valor))


def imprimir_dato(dato:str):
    print(dato)    

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
            for clave in mostrar_nombre_posicion(lista_jugadores):
                print(clave)
        case 2:
            while True:
                    mostrar_nombre_posicion(lista_jugadores)
                    mostrar_estadisticas(lista_jugadores)
        case 3:
            print(mostrar_logros(lista_jugadores))
        case 4:
            pass
        case 5:
            print("El promedio total de puntos por partidos del dream team es : {0}".format(calcular_promedio(lista_jugadores)))
            for clave in ivan_sort_A(crear_diccionario(lista_jugadores)):
                print(clave)
        case 6:
            pass
        case 7:
            calcular_y_mostrar_max_jugador(lista_jugadores, "rebotes_totales")
        case 8:
            calcular_y_mostrar_max_jugador(lista_jugadores, "porcentaje_tiros_de_campo")
        case 9:
            calcular_y_mostrar_max_jugador(lista_jugadores, "asistencias_totales")
        case 10:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"promedio_puntos_por_partido")
        case 11:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"promedio_rebotes_por_partido")
        case 12:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"asistencias_totales")
        case 13:
            calcular_y_mostrar_max_jugador(lista_jugadores,"robos_totales")
        case 14:
            pass
        case 15:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"porcentaje_tiros_libres")
        case 16:
            pass
        case 17:
            pass
        case 18:
            mostrar_jugadores_mayor_al_promedio(lista_jugadores,"porcentaje_tiros_triples")
        case 19:
            calcular_y_mostrar_max_jugador(lista_jugadores,"temporadas")
        case 20:
            pass
        case 23:
            pass
        case _:
            pass

while True :
    menu_final(lista_jugadores)
