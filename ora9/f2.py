my_dict = {}
print(my_dict,len(my_dict))
my_dict["kulcs"] = "érték"
my_dict["mouse"] = "egér"
print(my_dict,len(my_dict))
print("A cat értéke: ",my_dict["mouse"])
print(my_dict.get("dog"))