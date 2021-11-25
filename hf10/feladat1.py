
def input(users: dict):
    for i in range(2):
        name = input("Adjon meg egy nevet:\t")
        phone_numbers = input("Adjon meg egy telefonszámot:\t")
        answer = input("Szeretne még megadni telefonásmot?(igen/nem)\n")
        if answer == "igen":
            phone_numbers2 = input("Adjon meg egy telefonszámot:\t")
            users[name] = phone_numbers,phone_numbers2
        else:
            users[name] = phone_numbers

def ABC(users: dict):
    for key,value in sorted(users.items()):
        sorted(users.keys())
        print(key,value)

def require(users: dict):
    print(users.keys())
    name = input("adjon meg egy nevet a fentiekkből:\t")
    print(users[name])

users = {}
input(users)
ABC(users)
require(users)
