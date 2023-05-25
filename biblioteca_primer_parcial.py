import json
import re


def read_file(path_file: str) -> list:
    '''Levanta un archivo en formato json y lo devuelve como lista diccionario
    Param: La ruta del archivo
    Return: Una lista de diccioarios'''
    with open(path_file, 'r') as file_object:
        return json.load(file_object)['jugadores']
    
lista_jugadores_original = read_file("Repo_Github\pp_lab1_Bracuto_Lucas\dt.json")

def save_file(file_name_to_save : str,string_to_save : str) -> bool:
    '''Crea un archivo y guarda en él la informacion recibida por parametro
    Param: Un string con el nombre del archivo a guardar, Un string con la data a guardar
    Return: Un booleano'''
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

def show_dt_players(players_list : list) -> None:
    '''Muetra los nombres y la posicion de los integrantes del dream team
    Param: Una lista de jugadores
    Return: None'''
    string_players = ""
    if len(players_list) != 0:
        for index in range(len(players_list)):
            string_format = "{0:2} - Nombre: {1:20}- {2}\n=============================================\n"
            string_players += string_format.format(index,players_list[index]["nombre"],players_list[index]["posicion"])
        print_data("===============DREAM TEAM PLAYERS============")
        print_data(string_players)


#show_dt_players(lista_jugadores_original)

###2

def show_player_statistics_by_index(player_list : list) -> list:
    '''Selecciona un jugador por indice y lo muestra con todas sus caracteristicas
    Param: una lista de jugadores
    Return: una lista con el jugador ingresado por indice'''
    string_player = ""
    new_list = []
    if len(player_list) != 0:
        show_dt_players(player_list)
        index_chosen = input("=Ingrese el indice del jugador a mostrar: ")
        if re.match("^[0-9]{1,2}$",index_chosen) and int(index_chosen) <= len(player_list) and int(index_chosen) >= 0:
            new_list.append(player_list[int(index_chosen)])
            for statistics in player_list[int(index_chosen)]["estadisticas"]:  
                string_format = "{0:33}| {1}\n=============================================\n"             
                string_player += string_format.format(statistics.capitalize().replace("_"," "),player_list[int(index_chosen)]["estadisticas"][statistics])
            
            print_data("\n=============================================\n{3:2} - {0:28}| {1}\n=============================================\n{2}".format(player_list[int(index_chosen)]["nombre"],player_list[int(index_chosen)]["posicion"],string_player,int(index_chosen)))
        else:
            print_data("ERROR: Opcion invalida")
    else:
        print_data("ERROR: Lista vacia")
    return new_list
jugador = show_player_statistics_by_index(lista_jugadores_original)

##3

def save_player_in_csv(player_list : list[dict]) -> bool:
    '''Guarda en un archivo csv un jugador recibido como lista
    Param: Una lista con un jugador
    Return: True si sale todo bien, False si no'''
    function_return = False
    string_player = ""
    if len(player_list) != 0:
        string_player = "{0},{1}".format(player_list[0]["nombre"],player_list[0]["posicion"])
        for value in player_list[0]["estadisticas"].values():
            string_player += ",{0}".format(value)
    save_file("{0}_w_statistics.csv".format(player_list[0]["nombre"]).replace(" ","_"),string_player)

save_player_in_csv(jugador)