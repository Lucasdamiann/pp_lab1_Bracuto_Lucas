import json
import re


def read_file(path_file: str) -> list:
    '''Levanta un archivo en formato json y lo devuelve como lista diccionario
    Param: La ruta del archivo
    Return: Una lista de diccioarios'''
    with open(path_file, 'r') as file_object:
        return json.load(file_object)['jugadores']
    
lista_jugadores_original = read_file("Repo_Github\pp_lab1_Bracuto_Lucas\dt.json")

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

def show_player_statistics_by_index(player_list : list) ->None:
    '''Selecciona un jugador por indice y lo muestra con todas sus caracteristicas
    param: una lista de jugadores
    return: none'''
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

show_player_statistics_by_index(lista_jugadores_original)