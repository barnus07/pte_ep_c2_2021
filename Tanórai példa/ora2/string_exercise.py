python = "python"
print("A python szó 1. karaktere:", python[0])
print("A python szó utolsó karaktere:", python[-1])
print("A python szó utolsó karaktere:", python[len(python) - 1])
str2 = "hallgató"
str3 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
str2_position_in_str3 = str3.find(str2)
print(str3[str2_position_in_str3:str2_position_in_str3 + len(str2)])
str4 = "Elemi"
str5 = "programozás"
str6 = str4 + " " + str5
print(str4, str5)
print(str6)
