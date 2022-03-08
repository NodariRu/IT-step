my_dict = {
    "name":"nodo",
    "age": 22,
    "surname":"rusishvili",
    "children": ["gio", "sandro", "luka"],
    "location": "tbilisi"
}
my_dict["age"] = 32
print(my_dict)
my_dict.pop("location")
print(my_dict)
my_dict["has_gf"] = "True"
print(my_dict)
my_dict.clear()
print(my_dict)
