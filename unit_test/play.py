import requests
import random
from threading import Thread


def create_game():
    url = "http://106.75.33.221:6000/api/game"
    payload = "{'Map':'RectSmall'}}"
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return  response.text

def game_List():
    url = "http://106.75.33.221:6000/api/game"
    headers = {
        'Cache-Control': "no-cache",
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)

def join_game(game_id, player):
    url = "http://106.75.33.221:6000/api/game/"
    payload = f"{{'Game':'{game_id}', 'Player':'{player}'}}"
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }
    response = requests.request("PATCH", url, data=payload, headers=headers)
    print("playter", player)
    print(response.text)

def create_gamer(num=0):
    seed = [chr(i) for i in range(97,123)]
    seed = ''.join(seed)
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    player = ''.join(sa)+str(random.randint(0,99))
    url = "http://106.75.33.221:6000/api/player"
    payload = f"{{'Name':'{player}', 'Color':'{num}'}}"
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def start_game(game_id):
    url = "http://106.75.33.221:6000/api/game/{game_id}".format(game_id=game_id)
    print(url)
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("PUT", url, headers=headers)
    print("start")
    print(response.text)

def get_player(game_id):
    url = f"http://106.75.33.221:6000/api/player/{game_id}"
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)

def get_map(self):
    url = "http://106.75.33.221:6000/api/map/rectsmall"
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)

    print(response.text)

def attach(gamed_id, player):
    url = "http://106.75.33.221:6000/api/cell/"
    for x in range(100):
        payload = f"{{'Game':'{game_id}', 'Player':'{player}', 'X':'{x}', 'Y':'{x}'}}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        response = requests.request("PUT", url, data=payload, headers=headers)
        print(response.text, response.status_code)


game_id = create_game()
player1 = create_gamer(num=1)
player2 = create_gamer(num=2)
player1 = player1.split(",")[0].split(":")[1]
player2 = player2.split(",")[0].split(":")[1]
print(player1, player2)
join_game(game_id, player1)
join_game(game_id, player2)
start_game(game_id)


# t1 = Thread(name='attach1', target=attach, args=(game_id, player1,))
# t2 = Thread(name='attach2', target=attach, args=(game_id, player2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

