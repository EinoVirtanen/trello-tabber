import requests
import sys
import webbrowser

key = 'foo'
token = 'bar'
board = '5c7d287d3750205bd838ae41'

board_get_url = 'https://api.trello.com/1/boards/' + board + '/lists?key=' + key + '&token=' + token
response = requests.get(board_get_url)
listat = response.json()

for lista in listat:
    print(lista['name'], lista['id'])
    list_get_url = 'https://api.trello.com/1/lists/' + lista['id'] + '/cards?key=' + key + '&token=' + token
    print('list_get_url == ' + list_get_url)
    print('fetching cards..')
    cards_response = requests.get(list_get_url)
    print(cards_response)
    print('converting to json..')
    cards = cards_response.json()
    for card in cards:
        urli = card['url']
        print(urli)
        webbrowser.open_new_tab(urli)
