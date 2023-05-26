import json
import re


def read_file(path_file: str) -> list[dict]:
    '''Levanta un archivo en formato json y lo devuelve como lista diccionario
    Param: La ruta del archivo
    Return: Una lista de diccioarios'''
    with open(path_file, 'r', encoding="UTF-8") as file_object:
        return json.load(file_object)['jugadores']
    
lista_jugadores_original = read_file("Repo_Github\pp_lab1_Bracuto_Lucas\dt.json")

def save_file(file_name_to_save : str,string_to_save : str) -> bool:
    '''Crea un archivo y guarda en él la informacion recibida por parametro
    Param: Un string con el nombre del archivo a guardar, Un string con la data a guardar
    Return: True si sale todo bien, False si no'''
    function_return = False
    with open(file_name_to_save, 'w+') as file_object:
        if file_object.write (string_to_save):
            print_data("Se creó el archivo: {}".format(file_name_to_save))
            function_return = True        
        else:
            print_data("Error al crear el archivo: {}".format(file_name_to_save))            
    return function_return  

def print_data(string_received : str) -> None:
    '''Imprime el string recibido por parametro
    Param: Un string cualquiera
    Return: None''' 
    print(string_received)

###1

def show_dt_players(players_list : list[dict]) -> None:
    '''Muetra los nombres y la posicion de los integrantes del dream team
    Param: Una lista de jugadores
    Return: None'''
    string_players = ""
    if len(players_list) != 0:
        for player in players_list:
            string_format = "{0:2} - Nombre: {1:20}- {2}\n=============================================\n"
            string_players += string_format.format(players_list.index(player),player["nombre"],player["posicion"])
        print_data("===============DREAM TEAM PLAYERS============")
        print_data(string_players)

#vamos a empezar
#show_dt_players(lista_jugadores_original)

###2

def show_player_statistics_by_index(players_list : list[dict]) -> list[dict]:
    '''Selecciona un jugador por indice y lo muestra con todas sus caracteristicas
    Param: una lista de jugadores
    Return: una lista con el jugador ingresado por indice'''
    string_player = ""
    new_list = []
    if len(players_list) != 0:
        show_dt_players(players_list)
        index_chosen = input("=Ingrese el indice del jugador a mostrar: ")
        if re.match("^[0-9]{1,2}$",index_chosen) and int(index_chosen) <= len(players_list) and int(index_chosen) >= 0:
            new_list.append(players_list[int(index_chosen)])
            for statistics in players_list[int(index_chosen)]["estadisticas"]:  
                string_format = "{0:33}| {1}\n=============================================\n"             
                string_player += string_format.format(statistics.capitalize().replace("_"," "),players_list[int(index_chosen)]["estadisticas"][statistics])
            
            print_data("\n=============================================\n{3:2} - {0:28}| {1}\n=============================================\n{2}".format(players_list[int(index_chosen)]["nombre"],players_list[int(index_chosen)]["posicion"],string_player,int(index_chosen)))
        else:
            print_data("ERROR: Opcion invalida")
    else:
        print_data("ERROR: Lista vacia")
    return new_list
#jugador = show_player_statistics_by_index(lista_jugadores_original)

##3

def save_player_in_csv(players_list : list[dict]) -> bool:
    '''Guarda en un archivo csv un jugador recibido como lista
    Param: Una lista con un jugador
    Return: True si sale todo bien, False si no'''
    function_return = False
    string_player = ""
    if len(players_list) != 0:
        string_player = "{0},{1}".format(players_list[0]["nombre"],players_list[0]["posicion"])
        for value in players_list[0]["estadisticas"].values():
            string_player += ",{0}".format(value)
    if save_file("{0}_w_statistics.csv".format(players_list[0]["nombre"]).replace(" ","_"),string_player):
        function_return = True
    return function_return    

#save_player_in_csv(jugador)

###4
def capitalize_full_name(name : str) -> str:
    '''Capitaliza cada palabra de un string completo
    Param: Un string para capitalizar
    Return: Un string capitalizado'''
    splitted_string = name.split(" ")
    capitalized_string = ""
    for string in splitted_string:
        capitalized_string += "{0} ".format(string).capitalize()
    return  capitalized_string.strip()

def search_by_name_and_show_achievement(players_list : list[dict]) -> bool:
    '''Busca un jugador por nombre y muestra sus logros
    Param: Una lista de jugadores
    Return: True si sale todo bien, False si no'''
    function_return = False
    if len(players_list) != 0:
        chosen_name = input("Ingrese el nombre de un jugador: ")
        if re.search(r"^[a-zA-Z ]+$",chosen_name):
            capitalized_name = capitalize_full_name(chosen_name)
            for player in players_list:
                if re.match(capitalized_name,player["nombre"]):
                    string_achievement = "\n".join(player["logros"])
                    function_return = True
                    string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2}\n=============================================\n"
                    print_data(string_format.format(player["nombre"],player["posicion"],string_achievement))                    
                    break
            if not function_return:        
                print_data("ERROR: Nombre inexistente")                    
        else:
            print_data("ERROR: Caracteres incorrectos")    
    return function_return

#earch_by_name_and_show_achievement(lista_jugadores_original)

###5

def calculate_promedy_of_points_per_game(players_list :list[dict]) -> float:
    '''Calcula el promedo de puntos por partido de todo el equipo
    Param: Una lista de jugadores
    Return: El resultado del promedio como float'''
    acumulator = 0
    counter = 0
    if len(players_list) != 0:
        for player in players_list:
            if "promedio_puntos_por_partido" in player["estadisticas"]:
                acumulator += player["estadisticas"]["promedio_puntos_por_partido"]
                counter += 1
    return round(acumulator/counter,2)


def order_by_alphabetic_string(players_list : list[dict], players_key : str , order : bool = True) -> list[dict]:
    '''Ordena la lista por determinada key con valor string de manera descendente por defecto
    Param: Una lista de diccionarios, un string de key, un string de orden que por defecto es False
    Return: Una lista de diccionarios ordenada'''
    players_list_copy = players_list.copy()
    range_of_list = len(players_list_copy)
    flag_swap = True
    while flag_swap:
        flag_swap = False
        range_of_list = range_of_list-1
        for index in range(range_of_list):
            if (players_list_copy[index][players_key] > players_list_copy[index+1][players_key] and order == True)\
                  | (players_list_copy[index][players_key] < players_list_copy[index+1][players_key] and order == False):
                buffer = players_list_copy[index]
                players_list_copy[index],players_list_copy[index+1] = players_list_copy[index+1],buffer 
                flag_swap = True
    return players_list_copy

def order_alphabetically_by_name(players_list : list[dict]) -> list:
    '''Ordena alfabeticamente por nombre una lista de jugadores
    Param: Una lista de jugadores
    Return: Una lista de jugadores ordenada alfabeticamente'''
    if len(players_list) != 0:
        return order_by_alphabetic_string(players_list,"nombre",True) 

def show_player_w_promedy_of_points_per_game(players_list : list[dict]) -> bool:
    '''Muestra los jugadores con sus promedios de puntos por partido
    Param: Una lista de jugadores
    Return: True si sale todo bien, False si no'''
    string_player = ""
    if len(players_list) != 0:
        promedy = calculate_promedy_of_points_per_game(players_list)
        print_data("\n=============================================\n{0:33}| {1}\n=============================================\n".format("Promedio de puntos por partido DT", promedy))
        for player in players_list:          
            string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2:33}| {3}"
            string_player = string_format.format(player["nombre"],player["posicion"],"Promedio puntos por partido",player["estadisticas"]["promedio_puntos_por_partido"]) 
            print_data(string_player)

#lista_ordenada = order_alphabetically_by_name(lista_jugadores_original)

#show_player_w_promedy_of_points_per_game(lista_ordenada)

###6

def search_by_name_hall_of_fame_member(players_list : list[dict]) -> bool:
    '''Busca un jugador por nombre y muestra sus logros
    Param: Una lista de jugadores
    Return: True si sale todo bien, False si no'''
    function_return = False
    if len(players_list) != 0:
        chosen_name = input("Ingrese el nombre de un jugador: ")
        if re.search(r"^[a-zA-Z ]+$",chosen_name):
            capitalized_name = capitalize_full_name(chosen_name)
            hall_of_fame_string = "Miembro del Salon de la Fama del Baloncesto" 
            for player in players_list:
                if re.match(capitalized_name,player["nombre"]):                                       
                    if hall_of_fame_string in player["logros"]:
                        string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2}\n=============================================\n"
                        print_data(string_format.format(player["nombre"],player["posicion"],hall_of_fame_string))
                        function_return = True         
                        break                   
            if not function_return:        
                print_data("ERROR: No es Miembro del Salon de la Fama del Baloncesto")                    
        else:
            print_data("ERROR: Caracteres incorrectos")    
    return function_return

#search_by_name_hall_of_fame_member(lista_jugadores_original)

###7

def calculate_player_w_most_quantity_of_selected_statistic(players_list : list[dict], statistic : str) -> list[dict]:
    '''Calcula el jugador con la mayor cantidad de la estadistica elegida
    Param: Una lista de jugadores, un string con el nombre de una estadistica
    Return: Una lista con el jugador que cumple el requisito'''
    function_return = "ERROR"
    new_list = []
    if len(players_list) != 0:
        higher_statistic = players_list[0]["estadisticas"][statistic]
        for index in range(len(players_list)):
            if players_list[index]["estadisticas"][statistic] > higher_statistic :
                higher_statistic = players_list[index]["estadisticas"][statistic]
                higher_player = players_list[index]
        new_list.append(higher_player)
        function_return = new_list
    return function_return                    


def show_player_received(players_list : list[dict], statistic : str) -> None:
    '''Muestra un jugador con su estadistica elegida
    Para: Un diccionario de un jugador
    Return: None'''
    string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2:33}| {3}\n=============================================\n"
    print_data(string_format.format(players_list[0]["nombre"],players_list[0]["posicion"],statistic.replace("_"," ").capitalize(),players_list[0]["estadisticas"][statistic]))


#diccionario = calculate_player_w_most_quantity_of_selected_statistic(lista_jugadores_original,"rebotes_totales")
#show_player_received(diccionario,"rebotes_totales")

###8

#diccionario = calculate_player_w_most_quantity_of_selected_statistic(lista_jugadores_original,"porcentaje_tiros_de_campo")
#show_player_received(diccionario,"porcentaje_tiros_de_campo")

###9

#diccionario = calculate_player_w_most_quantity_of_selected_statistic(lista_jugadores_original,"asistencias_totales")
#show_player_received(diccionario,"asistencias_totales")

###10

def show_players_w_more_quantity_of_selected_statistic(players_list : list[dict], statistic : str) -> None:
    '''Muestra los jugadores que tengan una cantidad superior al numero ingresado de una determinada caracteristica
    Param: Una lista de jugadores, un string con el nombre de una estadistica
    Return: None'''
    new_list = []
    string_player = ""
    if len(players_list) != 0:
        ingressed_value = input("Mostrar jugador/es cuyo numero de [{0}] sea mayor a: ".format(statistic.replace("_"," ")))
        for player in players_list:
            if re.match(r"^[0-9]+.{1}[0-9]+$|^[0-9]+",ingressed_value) and player["estadisticas"][statistic] > float(ingressed_value):
                new_list.append(player)
                string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2:33}| {3}\n=============================================\n"
                string_player += string_format.format(player["nombre"],player["posicion"],statistic.replace("_"," ").capitalize(),player["estadisticas"][statistic])
        print_data(string_player)

#show_players_w_more_quantity_of_selected_statistic(lista_jugadores_original ,"promedio_puntos_por_partido")

###11

#show_players_w_more_quantity_of_selected_statistic(lista_jugadores_original ,"promedio_rebotes_por_partido")

###12

#show_players_w_more_quantity_of_selected_statistic(lista_jugadores_original ,"promedio_asistencias_por_partido")

###13

#diccionario = calculate_player_w_most_quantity_of_selected_statistic(lista_jugadores_original,"robos_totales")
#show_player_received(diccionario,"robos_totales")

###14

#diccionario = calculate_player_w_most_quantity_of_selected_statistic(lista_jugadores_original,"bloqueos_totales")
#show_player_received(diccionario,"bloqueos_totales")

###15

#show_players_w_more_quantity_of_selected_statistic(lista_jugadores_original ,"porcentaje_tiros_libres")

###16

def exclude_the_worst_scorer(players_list : list[dict]) -> list[dict]:
    '''Crea una lista filtrando al jugador con menos cantidad de puntos por partido
    Param: Una lista de jugadores
    Return: Una lista de jugadores sin el jugador con menos cantidad de puntos por partido'''
    players_list_copy = players_list.copy()
    if len(players_list) != 0:
        lower_statistic = players_list[0]["estadisticas"]["promedio_puntos_por_partido"]
        for index in range(len(players_list)):
            if players_list[index]["estadisticas"]["promedio_puntos_por_partido"] < lower_statistic :
                lower_statistic = players_list[index]["estadisticas"]["promedio_puntos_por_partido"]
                lower_player = players_list[index]    
        players_list_copy.remove(lower_player)    
    return players_list_copy

show_player_w_promedy_of_points_per_game(exclude_the_worst_scorer(lista_jugadores_original))
