import json
import re
import csv
import os
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
    for jugador in lista_jugadores:
        print("{0} | {1}".format(jugador["nombre"],jugador["posicion"]))


def mostrar_estadisticas(lista_jugadores: list):
    '''
    Crea una lista de datos y la exporta a un archivo csv
    Recibe una lista
    '''
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
        nombre_archivo = "estadisticas.csv"
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
    promedios_puntos = []
    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        promedios_punto = jugador["estadisticas"]["promedio_puntos_por_partido"]
        nombre_y_promedio= ("{0}:{1}".format(nombre,promedios_punto))
        promedios_puntos.append(nombre_y_promedio)

    return promedios_puntos




def calcular_y_mostrar_max_jugador(lista_jugadores, clave):
    '''
    Calcula y muestra el máximo valor de una clave en la lista
    Recibe una lista
    '''
    if len(lista_jugadores) == 0:
        return lista_jugadores

    maximo = 0
    jugadores_maximos = []

    for jugador in lista_jugadores:
        if "estadisticas" in jugador and clave in jugador["estadisticas"]:
            valor = jugador["estadisticas"][clave]
            if valor > maximo:
                maximo = valor
                jugadores_maximos = [jugador["nombre"]]
            elif valor == maximo:
                jugadores_maximos.append(jugador["nombre"])

    if jugadores_maximos:
        clave_validada = re.sub("_", " ", clave)
        print("Jugadores con más {0}:".format(clave_validada))
        for jugador in jugadores_maximos:
            print("{0} | {1}: {2}".format(jugador, clave_validada, maximo))



def mostrar_logros(lista_jugadores:list)->list:
    '''
    Busca un jugador por su nombre, lo agrega a lista y muestra sus logros
    Recibe una lista
    Retorna una lista
    '''
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
    if len(lista_jugadores) == 0:
        return lista_jugadores

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
    if len(lista_jugadores) == 0:
        return lista_jugadores
    valor = input("Ingrese un valor numerico: ")
    valor_float = float(re.sub(",",".",valor))
    


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
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
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
    if len(lista_jugadores) == 0:
        return lista_jugadores
    jugadores_filtrados = []

    for jugador in lista_jugadores:
        porcentaje_tiros_de_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if porcentaje_tiros_de_campo > porcentaje:
            jugadores_filtrados.append(jugador)  

    rango = len(jugadores_filtrados)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango -= 1
        for indice in range(rango):
            if jugadores_filtrados[indice]["posicion"] > jugadores_filtrados[indice + 1]["posicion"] :
                jugadores_filtrados[indice],jugadores_filtrados[indice + 1] = jugadores_filtrados[indice + 1],jugadores_filtrados[indice]
                flag_swap = True
    return jugadores_filtrados
   
def mostrar_jugadores_con_porcentaje_superior(lista_jugadores:list):  
    '''
    Muestra los jugadores con mayor porcentaje que el valor ingresado
    Recibe una lista
    Retorna una lista ordenada
    '''    
    if len(lista_jugadores) == 0:
        return lista_jugadores
    porcentaje = input("Ingrese un valor numerico: ")
    porcentaje_float = float(re.sub(",",".",porcentaje))

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
        print("No se encontraron jugadores con promedio  mayor que {0}.".format(porcentaje_float))

    return jugadores_filtrados    
def contar_por_posicion(lista_jugadores):
    posiciones = {}
    for jugador in lista_jugadores:
        clave = jugador["posicion"]
        if clave in posiciones:
            posiciones[clave] += 1  
        else:
            posiciones[clave] = 1 
    return posiciones

#print(contar_por_posicion(lista_jugadores))        


def quick_sort_dicts(lista:list, clave: str, asc:bool = True)->list:
  

    lista_de = []
    lista_iz = []
    if(len(lista)<=1):
        return lista

    pivot_encontrado = False

    for elemento in lista:
        for clave_elemento, valor_elemento in elemento.items():
            if clave in valor_elemento:
                if not pivot_encontrado:
                    pivot = elemento
                    pivot_encontrado = True
                else:
                    if type(valor_elemento) == type(dict()):
                        if asc and valor_elemento[clave] > pivot[clave_elemento][clave] or \
                                not asc and valor_elemento[clave] < pivot[clave_elemento][clave]:
                            lista_de.append(elemento)
                        else:
                            lista_iz.append(elemento)

    lista_iz = quick_sort_dicts(lista_iz, clave, asc)
    lista_iz.append(pivot)
    lista_de = quick_sort_dicts(lista_de, clave, asc)

    lista_iz.extend(lista_de)
    lista_ordenada = lista_iz
    return lista_ordenada
def exportar_rankings_a_csv(lista_jugadores):
    '''
    Crea y ordena las listas de estadisticas en orden descendente. Se crea la lista del ranking de los jugadores,se itera cada jugador
    de la lista de jugadores y se agrega al diccionario de posiciones, se itera cada de indice de las listas de estadisticas
    si coincide en nombre del jugador con la lista que se esta iterando se agrega al diccionario y su posicion. Luego se agrega
    todo el diccionario a la lista de ranking. Luego se genera un archivo csv con las posiciones en el ranking de cada jugador.
    Recibe una lista
    Retorna una lista
    
    '''
    puntos_ordenados = quick_sort_dicts(lista_jugadores,"puntos_totales",False)
    rebotes_ordenados = quick_sort_dicts(lista_jugadores,"rebotes_totales",False)
    asistencias_ordenadas = quick_sort_dicts(lista_jugadores,"asistencias_totales",False)
    robos_ordenados = quick_sort_dicts(lista_jugadores,"robos_totales",False)

    ranking_jugadores = []
    for jugador in lista_jugadores:
        posiciones_en_ranking = {}
        for indice in range(len(puntos_ordenados)):
            if jugador["nombre"] == puntos_ordenados[indice]["nombre"]:
                posiciones_en_ranking["jugador"] = puntos_ordenados[indice]["nombre"]
                posiciones_en_ranking["puntos"] = indice + 1
                break
    
        for indice in range(len(rebotes_ordenados)):
            if jugador["nombre"] == rebotes_ordenados[indice]["nombre"]:
                posiciones_en_ranking["rebotes"] = indice + 1
                break  

        for indice in range(len(asistencias_ordenadas)):
            if jugador["nombre"] ==asistencias_ordenadas[indice]["nombre"]:
                posiciones_en_ranking["asistencias"] = indice + 1
                break      
        for indice in range(len(robos_ordenados)):
            if jugador["nombre"] == robos_ordenados[indice]["nombre"]:
                posiciones_en_ranking["robos"] = indice + 1
                break         
        ranking_jugadores.append(posiciones_en_ranking)  

    with open("ranking_jugadores.csv", "w") as archivo_csv:
        archivo_csv.write("Puntos   Rebotes   Asistencias   Robos   Jugador\n")
        for jugador in ranking_jugadores:
            linea = "{:<10}{:<12}{:<12}{:<7}{}\n".format(jugador["puntos"], jugador["rebotes"], jugador["asistencias"], jugador["robos"], jugador["jugador"])
            archivo_csv.write(linea)

        if "ranking_jugadores.csv":
            return print("Archivo guardado correctamente")
        else:
            return print("Error") 








def calcular_mejores_estadisticas(lista_jugadores):
    jugador_maximo = None
    puntaje_maximo = 0

    for jugador in lista_jugadores:
        estadisticas = 0
        for estadistica in jugador["estadisticas"].values():
            estadisticas += estadistica
        if jugador_maximo is None or estadisticas > puntaje_maximo:
            jugador_maximo = jugador
            puntaje_maximo = estadisticas

    return jugador_maximo
#print(calcular_mejores_estadisticas(lista_jugadores))                  


    
    
    

def menu():
    menu = "1 - Mostrar todos los jugadores del Dream Team\n"\
    "2 - Mostrar estadísticas de un jugador\n"\
    "3 - Buscar un jugador por su nombre y mostrar sus logros\n"\
    "4 - Mostrar prome0dio de puntos por partido de todo el Dream Team\n"\
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
    "23 - BONUS !!! Mostrar la posición de cada jugador en los siguientes rankings:Puntos, Rebotes, Asistencias y Robos\n"\
    "0 - Salir\n"\
    

    
    print( menu)
    

def opcion_elegida():
    opcion = input("Ingrese una opción: ")
    while not re.match(r"^(0|[1-9]|2[0-9])$", opcion):
        print("Opción inválida. Intente nuevamente.")
        opcion = input("Ingrese una opción: ")
    return int(opcion)


while True:
    menu()
    opcion = opcion_elegida()
    match(opcion):
            case 0:
                os.system("cls")
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
                exportar_rankings_a_csv(lista_jugadores)
            case 24:
                print(contar_por_posicion(lista_jugadores))
            case 25:
                pass
            case 26:
                calcular_y_mostrar_max_jugador(lista_jugadores,"temporadas")
                calcular_y_mostrar_max_jugador(lista_jugadores,"puntos_totales")
                calcular_y_mostrar_max_jugador(lista_jugadores,"promedio_puntos_por_partido")
                calcular_y_mostrar_max_jugador(lista_jugadores,"rebotes_totales")
                calcular_y_mostrar_max_jugador(lista_jugadores,"promedio_rebotes_por_partido")
                calcular_y_mostrar_max_jugador(lista_jugadores,"asistencias_totales")
                calcular_y_mostrar_max_jugador(lista_jugadores,"promedio_asistencias_por_partido")
                calcular_y_mostrar_max_jugador(lista_jugadores,"robos_totales")
                calcular_y_mostrar_max_jugador(lista_jugadores,"bloqueos_totales")
                calcular_y_mostrar_max_jugador(lista_jugadores,"porcentaje_tiros_de_campo")
                calcular_y_mostrar_max_jugador(lista_jugadores,"porcentaje_tiros_libres")
                calcular_y_mostrar_max_jugador(lista_jugadores,"porcentaje_tiros_triples")
                
            case 27:
                print(calcular_mejores_estadisticas(lista_jugadores))    
                    


