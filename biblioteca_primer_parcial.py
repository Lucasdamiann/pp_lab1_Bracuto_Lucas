import json
import os
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

def limpiar_consola() -> None:
    """
    This function clears the console screen and waits for user input to continue.
    """
    _ = input('\nPresione [Enter] para volver al menu ')
    if os.name in ['ce', 'nt', 'dos']: os.system("cls")
    else: os.system("clear")

################################################1

def show_dt_players(players_list : list[dict]) -> None:
    '''Muetra los nombres y la posicion de los integrantes del dream team
    Param: Una lista de jugadores
    Return: None'''
    string_players = ""
    if len(players_list) != 0:
        for player in players_list:
            string_format = "{0:2} - Nombre: {1:20}- {2}\n=============================================\n"
            string_players += string_format.format(players_list.index(player),player["nombre"],player["posicion"])
        print_data("\n===============DREAM TEAM PLAYERS============")
        print_data(string_players)

################################################2

def show_player_statistics_by_index(players_list : list[dict]) -> list[dict]:
    '''Selecciona un jugador por indice y lo muestra con todas sus caracteristicas
    Param: una lista de jugadores
    Return: una lista con el jugador ingresado por indice'''
    string_player = ""
    new_list = []
    if len(players_list) != 0:
        show_dt_players(players_list)
        index_chosen = input("\nIngrese el indice del jugador a mostrar: ")
        if re.match("^[0-9]{1,2}$",index_chosen) and int(index_chosen) <= len(players_list) and int(index_chosen) >= 0:
            new_list.append(players_list[int(index_chosen)])
            for statistics in players_list[int(index_chosen)]["estadisticas"]:  
                string_format = "{0:33}| {1}\n=============================================\n"             
                string_player += string_format.format(statistics.capitalize().replace("_"," "),players_list[int(index_chosen)]["estadisticas"][statistics])
            
            print_data("\n=============================================\n{3:2} - {0:28}| {1}\n=============================================\n{2}".format(players_list[int(index_chosen)]["nombre"],players_list[int(index_chosen)]["posicion"],string_player,int(index_chosen)))
        else:
            print_data("\n======================\nERROR: Opcion invalida\n======================\n")
    else:
        print_data("\n==================\nERROR: Lista vacia\n==================\n")
    return new_list

################################################3

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

################################################4

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
        chosen_name = input("\nIngrese el nombre de un jugador: ")
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
                print_data("\n=========================\nERROR: Nombre inexistente\n=========================\n")                    
        else:
            print_data("\n=============================\nERROR: Caracteres incorrectos\n=============================\n")    
    return function_return

################################################5

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

def order_alphabetically_by_key(players_list : list[dict], player_key :str) -> list:
    '''Ordena alfabeticamente por nombre una lista de jugadores
    Param: Una lista de jugadores
    Return: Una lista de jugadores ordenada alfabeticamente'''
    if len(players_list) != 0:
        return order_by_alphabetic_string(players_list,player_key,True) 

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

################################################6

def search_by_name_hall_of_fame_member(players_list : list[dict]) -> bool:
    '''Busca un jugador por nombre y muestra sus logros
    Param: Una lista de jugadores
    Return: True si sale todo bien, False si no'''
    function_return = False
    if len(players_list) != 0:
        chosen_name = input("\nIngrese el nombre de un jugador: ")
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
                print_data("\n========================================================\nERROR: No es Miembro del Salon de la Fama del Baloncesto \n========================================================\n")                    
        else:
            print_data("\n=============================\nERROR: Caracteres incorrectos\n=============================\n")    
    return function_return

################################################7
################################################8
################################################9
################################################13
################################################14
################################################19
################################################20

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


def show_player_received_w_statistic(players_list : list[dict], statistic : str) -> None:
    '''Muestra un jugador con su estadistica elegida
    Para: Un diccionario de un jugador
    Return: None'''
    string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2:33}| {3}\n=============================================\n"
    print_data(string_format.format(players_list[0]["nombre"],players_list[0]["posicion"],statistic.replace("_"," ").capitalize(),players_list[0]["estadisticas"][statistic]))

################################################10
################################################11
################################################12
################################################15
################################################18

def show_players_w_more_quantity_of_selected_statistic(players_list : list[dict], statistic : str) -> None:
    '''Muestra los jugadores que tengan una cantidad superior al numero ingresado de una determinada caracteristica
    Param: Una lista de jugadores, un string con el nombre de una estadistica
    Return: None'''
    new_list = []
    string_player = ""
    if len(players_list) != 0:
        ingressed_value = input("\nMostrar jugador/es cuyo numero de [{0}] sea mayor a: ".format(statistic.replace("_"," ")))
        for player in players_list:
            if re.match(r"^[0-9]+.{1}[0-9]+$|^[0-9]+",ingressed_value) and player["estadisticas"][statistic] > float(ingressed_value):
                new_list.append(player)
                string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n{2:33}| {3}\n=============================================\n"
                string_player += string_format.format(player["nombre"],player["posicion"],statistic.replace("_"," ").capitalize(),player["estadisticas"][statistic])
        if len(new_list) == 0:
            string_player = "\n==========================================\nNo hay jugador que cumpla con esa cantidad\n==========================================\n"
        print_data(string_player)

################################################16

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

################################################17

def calculate_player_w_most_quantity_of_achievements(players_list : list[dict]) -> list[dict]:
    '''Calcula el jugador con la mayor cantidad de logros
    Param: Una lista de jugadores
    Return: Una lista con el jugador que cumple el requisito'''
    function_return = "ERROR"
    new_list = []
    if len(players_list) != 0:
        higher_statistic = players_list[0]["logros"]
        higher_player = players_list[0]
        for index in range(len(players_list)):
            if len(players_list[index]["logros"]) > len(higher_statistic) :
                higher_statistic = players_list[index]["logros"]
                higher_player = players_list[index]
        new_list.append(higher_player)
        function_return = new_list
    return function_return                    


def show_player_received_w_achievement(players_list : list[dict]) -> None:
    '''Muestra un jugador con su estadistica elegida
    Para: Un diccionario de un jugador
    Return: None'''
    string_format = "\n=============================================\n{0:33}| {1}\n=============================================\n"
    string_name_position = string_format.format(players_list[0]["nombre"],players_list[0]["posicion"])
    print_data(string_name_position)
    for achievement in players_list[0]["logros"]:
        string_player = "{0}\n=============================================".format(achievement)
        print_data(string_player)

### MENU

def print_menu_options() -> None:    
    '''Imprime un menu
    Param: None
    Return: None'''
    menu =\
    '''
    MENU PRINCIPAL
    ============================================================================================
    1- Mostrar la lista de todos los jugadores del Dream Team
    ============================================================================================
    2- Seleccionar un jugador por su índice y mostrar sus estadísticas
    ============================================================================================
    3- Guardar las estadísticas del jugador anterior en un archivo CSV
    ============================================================================================
    4- Buscar un jugador por su nombre y mostrar sus logros
    ============================================================================================
    5- Mostrar el promedio de puntos por partido del Dream Team
    ============================================================================================
    6- Verificar con nombre si es miembro del Salón de la Fama del Baloncesto
    ============================================================================================
    7- Mostrar el jugador con la mayor cantidad de rebotes totales
    ============================================================================================
    8- Mostrar el jugador con el mayor porcentaje de tiros de campo
    ============================================================================================
    9- Mostrar el jugador con la mayor cantidad de asistencias totales
    ============================================================================================
    10- Ingresar un valor y mostrar los jugadores con más puntos por partido
    ============================================================================================
    11- Ingresar un valor y mostrar los jugadores con más rebotes por partido
    ============================================================================================
    12- Ingresar un valor y mostrar los jugadores con más asistencias por partido
    ============================================================================================
    13- Mostrar el jugador con la mayor cantidad de robos totales
    ============================================================================================
    14- Mostrar el jugador con la mayor cantidad de bloqueos totales
    ============================================================================================
    15- Ingresar un valor y mostrar los jugadores con mayor porcentaje de tiros libres
    ============================================================================================
    16- Mostrar el promedio de puntos por partido del equipo (sin el jugador con menos puntos)
    ============================================================================================
    17- Mostrar el jugador con la mayor cantidad de logros obtenidos
    ============================================================================================
    18- Ingresar un valor y mostrar los jugadores con mayor porcentaje de tiros triples
    ============================================================================================
    19- Mostrar el jugador con la mayor cantidad de temporadas jugadas
    ============================================================================================
    20- Ingresar un valor y mostrar los jugadores con mayor porcentaje de tiros de campo
    ============================================================================================
    23-BONUS- RANKING DE JUGADORES
    ============================================================================================
    0- Salir del programa
    ============================================================================================
    ''' 
    print_data(menu)

def selection_menu_options() -> int:
    '''Imprime un menu y captura el dato ingresado como opcion
    Param: None
    Return: La opcion elegida si sale bien, -1 si sale mal'''
    print_menu_options()
    option = input("Ingrese una opcion: ")
    if re.match("^[0-9]{1,2}$",option) and int(option) >= 0 and int(option) < 21 or int(option) == 23:
        return option
    return -1

def main_menu(players_list : list) -> None:
    '''Realiza la ejecucion de procesos de acuerdo a las opciones del menu solicitadas
    Param: Una lista de heroes
    Return: None'''
    players_list_copy = players_list.copy()    
    flag_second_option = False   
    while True: 
        option = selection_menu_options()   
        if option == "1":            
            show_dt_players(players_list_copy)     
            limpiar_consola()     
        elif option == "2":             
            player_selected = show_player_statistics_by_index(players_list_copy)
            flag_second_option = True
            limpiar_consola()  
        elif option == "3": 
            if flag_second_option:  
                save_player_in_csv(player_selected)  
                flag_second_option = False  
                limpiar_consola()      
            else:
                print_data("\n===========================================================\nERROR: Seleccionar jugador previamente para poder guardarlo\n===========================================================\n")    
                limpiar_consola()   
        elif option == "4":
            show_dt_players(players_list_copy)
            search_by_name_and_show_achievement(players_list_copy) 
            limpiar_consola()  
        elif option == "5":
            show_player_w_promedy_of_points_per_game(order_alphabetically_by_key(players_list_copy,"nombre"))
            limpiar_consola()  
        elif option == "6":
            show_dt_players(players_list_copy)
            search_by_name_hall_of_fame_member(players_list_copy)          
            limpiar_consola()  
        elif option == "7": 
            show_player_received_w_statistic(calculate_player_w_most_quantity_of_selected_statistic(players_list_copy,"rebotes_totales"),"rebotes_totales")
            limpiar_consola()  
        elif option == "8":
            show_player_received_w_statistic(calculate_player_w_most_quantity_of_selected_statistic(players_list_copy,"porcentaje_tiros_de_campo"),"porcentaje_tiros_de_campo")  
            limpiar_consola()            
        elif option == "9":
            show_player_received_w_statistic(calculate_player_w_most_quantity_of_selected_statistic(players_list_copy,"asistencias_totales"),"asistencias_totales")   
            limpiar_consola()                   
        elif option == "10": 
            show_players_w_more_quantity_of_selected_statistic(players_list_copy ,"promedio_puntos_por_partido") 
            limpiar_consola()  
        elif option == "11":    
            show_players_w_more_quantity_of_selected_statistic(players_list_copy ,"promedio_rebotes_por_partido")
            limpiar_consola()  
        elif option == "12":
            show_players_w_more_quantity_of_selected_statistic(players_list_copy ,"promedio_asistencias_por_partido")      
            limpiar_consola()     
        elif option == "13":
            show_player_received_w_statistic(calculate_player_w_most_quantity_of_selected_statistic(players_list_copy,"robos_totales"),"robos_totales")
            limpiar_consola()  
        elif option == "14":
            show_player_received_w_statistic(calculate_player_w_most_quantity_of_selected_statistic(players_list_copy,"bloqueos_totales"),"bloqueos_totales")
            limpiar_consola()  
        elif option == "15":
            show_players_w_more_quantity_of_selected_statistic(players_list_copy ,"porcentaje_tiros_libres")     
            limpiar_consola()       
        elif option == "16": 
            show_player_w_promedy_of_points_per_game(exclude_the_worst_scorer(players_list_copy))
            limpiar_consola()  
        elif option == "17":    
            show_player_received_w_achievement(calculate_player_w_most_quantity_of_achievements(players_list_copy))
            limpiar_consola()  
        elif option == "18":
            show_players_w_more_quantity_of_selected_statistic(players_list_copy ,"porcentaje_tiros_triples")     
            limpiar_consola()  
        elif option == "19": 
            show_players_w_more_quantity_of_selected_statistic(players_list_copy ,"temporadas")
            limpiar_consola()  
        elif option == "20":    
            show_players_w_more_quantity_of_selected_statistic(order_alphabetically_by_key(players_list_copy,"posicion") ,"porcentaje_tiros_de_campo")
            limpiar_consola()  
        elif option == "23":
            ranking(players_list_copy)
            limpiar_consola()
        elif option == "0":
            print_data("\n=====================\nSaliendo del programa\n=====================\n")
            break
        else:
            print_data("\n=================\nOpcion Incorrecta\n=================\n")
            limpiar_consola()

###23 Bonus
def sort_by_statistics(players_list : list[dict], players_key : str ) -> list[dict]:
    '''Ordena la lista por determinada key con valor numerico
    Param: Una lista de diccionarios, un string de key valida
    Return: Una lista de diccionarios ordenada'''
    players_list_copy = players_list.copy()
    range_of_list = len(players_list_copy)
    flag_swap = True
    while flag_swap:                
        flag_swap = False
        range_of_list -= 1 
        for index in range(range_of_list):  
            if players_key in players_list_copy[index]["estadisticas"]:                
                if (players_list_copy[index]["estadisticas"][players_key] < players_list_copy[index+1]["estadisticas"][players_key]):                
                    buffer = players_list_copy[index]
                    players_list_copy[index],players_list_copy[index+1] = players_list_copy[index+1],buffer 
                    flag_swap = True                 
    return players_list_copy

def ranking(players_list : list[dict]) -> None:
    '''Realiza un ranking de todos los jugadores en determinados estadisticas
    Param: Una lista de jugadores
    Return: None'''
    string_players = ""
    if len(players_list) != 0:
        points_list = sort_by_statistics(players_list,"puntos_totales")
        rebounces_list = sort_by_statistics(players_list,"rebotes_totales")
        assists_list = sort_by_statistics(players_list,"asistencias_totales")
        robberies_list = sort_by_statistics(players_list,"robos_totales")
        string_header = "\nRANKING\n=================================================\n{0:15}|{1:6}|{2:3}|{3:3}|{4:3}\n=================================================".format("Jugador","Puntos","Rebotes","Asistencias","Robos")
        print(string_header)
        for player in players_list:
            string_format = "\n=================================================\n{0:15}|{1:3}   |{2:4}   |{3:6}     |{4:3} \n=================================================\n"
            string_players += string_format.format(player["nombre"],points_list.index(player),rebounces_list.index(player),assists_list.index(player),robberies_list.index(player))
    print(string_players)
