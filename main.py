users:list = [
    {"name":"Julia","location":"Białobrzegi","posts":400},
    {"name":"Krzysztof","location":"Białobrzegi","posts":500},
    {"name":"Maja","location":"Swiecie","posts":300},
    {"name":"Zuzanna","location":"Białobrzegi","posts":700},
]




def get_user_info(users_data:list)->None:

    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowosci {user['location']} opublikowal {user['posts']} postów")

get_user_info(users)
