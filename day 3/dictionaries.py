
my_dict = {
    "name":"nodo",
    "age": 22,
    "surname":"rusishvili",
    "children": ["gio", "sandro", "luka"],
    "location": "tbilisi"
}

# key:value
# dictionary is ordered 
# changable
# no duplicates
print(my_dict["children"][3])
my_dict.pop("name")
print(my_dict)

couple_dict = {
    "nika":{
        "age": 22,
        "surname": "keshelava"
    },
      "mariami":{
          "age": 25,
        "surname": "ksovreli"
    }
}