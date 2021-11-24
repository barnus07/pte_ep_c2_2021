users = {}
for i in range(2):
    name = input("Adjon meg egy nevet:\t")
    phone_numbers = input("Adjon meg egy telefonszámot:\t")
    answer = input("Szeretne még megadni telefonásmot?(igen/nem)\n")
    if answer == "igen":
        phone_numbers2 = input("Adjon meg egy telefonszámot:\t")
        users[name] = phone_numbers,phone_numbers2
    else:
        users[name] = phone_numbers
print("A lista nevei:\n",list(users))
name = input("adjon meg egy nevet a listából:\t")
print(users.get(name))