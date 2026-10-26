# Working with Dictionaries
from pyscript import display, document



def game_details(e):
    document.getElementById('result').innerHTML =' '
    favorite_game = document.getElementById('dictionary').value.lower().strip()

    game_developers = {
    'roblox': 'David Baszucki',
    'codm': 'Timi Studio',
    'fnaf': 'Scott Cawthon',
    'minecraft': 'Notch',
    } # specifying dictonaries

    game_check = favorite_game in game_developers

    display_message = ('Sorry, your game is not in the list'
    , f'(game_developers)')

    display(display_message[game_check], target='result')

    game_developers['genshin impact'] = 'Hoyoverse' # adding a new element



    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_with_strings = ('ab', 'cd', 'ef')
    list_with_strings = ['ax', 'by', 'cz']


    display(dict(list_with_tuples), target='result')
    display(dict(list_with_strings), target='result')
    display(dict(tuple_with_strings), target='result')

    keywords = ['say', 'jm', 'jay', 'mace']
    values = ['Esguerra', 'Piansay', 'Estrada', 'Panela']

    students_nicknames = dict(zip(keywords, values))

    display(students_nicknames, target='result')

    philadelphia =  {
        'c': 'Joel Embiid',
        'pf': 'Lebron James',
        'sf': 'Jaylen Brown',
        'sg': 'VJ Edgecomb',
        'pg': 'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry' # updating
    del philadelphia['sg'] # deleting
    display(philadelphia, target='result')

    dict1 = {'x':1, 'y':2, 'z':3}
    dict2 = {'a':4, 'b':5, 'c':6}

    display(dict1 | dict2, target='result') # combining
    merged_dictionary = {**dict1, **dict2} # combining with asterisk
    display(merged_dictionary, target='result')
    display(len(merged_dictionary), target='result') # counting

    ai = {
        'tony stark': "creator",
        'JARVIS': 'AI1',
        'FRIDAY': 'AI2',
        'EDITH': 'AI3',
        'VISION': 'AI4'
        }

    display('VISION' in ai, target='result') # checking
    display(ai.get('JARVIS'), target='result') # getting the value
    display(ai.keys(), target='result') # getting all the keywords
    display(ai.values(), target='result') # getting all the values
    display(ai['tony stark'], target='result')
    display(ai['tony stark'], target='result')