import json


def read_file(path_file: str) -> list:
    '''Levanta un archivo en formato json y lo devuelve como lista diccionario
    Param: La ruta del archivo
    Return: Una lista de diccioarios'''
    with open(path_file, 'r') as file_object:
        return json.load(file_object)['jugadores']
    
lista_jugadores_original = read_file("primer_parcial\dt.json")

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
        for player in players_list:
            string_players += "Nombre: {0} - {1}\n".format(player["nombre"],player["posicion"])
        print_data(string_players)


show_dt_players(lista_jugadores_original)