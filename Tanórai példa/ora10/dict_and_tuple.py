my_tuple = ()
print(my_tuple, len(my_tuple))
my_tuple = (1, 2, 3)
print(my_tuple, len(my_tuple))

my_dict = {}
print(my_dict, len(my_dict))
my_dict["kulcs"] = "érték"
my_dict["mouse"] = "egér"
my_dict["cat"] = "macska"
print(my_dict, len(my_dict))
print("A cat értéke:", my_dict["cat"])
print("A dog értéke:", my_dict.get("dog", "Nem ismerem ezt a szót."))
print("A cat értéke:", my_dict.get("cat"))
print(my_dict.keys(), type(my_dict.keys()))
print(my_dict.values(), type(my_dict.values()))
print("Taralmazza a szótárunk a dog kulcsot:", "dog" in my_dict)
print("Taralmazza a szótárunk a cat kulcsot:", "cat" in my_dict)
print(my_dict.items(), type(my_dict.items()))
my_dict2 = my_dict.copy()
my_dict3 = my_dict2
my_dict2["dog"] = "kutya"
print(my_dict)
print(my_dict2)
print(my_dict3)
del(my_dict3["dog"])
print(my_dict)
print(my_dict2)
print(my_dict3)
my_dict3.clear()
print(my_dict)
print(my_dict2)
print(my_dict3)
