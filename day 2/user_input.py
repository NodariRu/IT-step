# name = input("enter your name: ")
# surname = input("enter your surname: ")

# print(name, surname)

#შემოვა ორი რიცხვი input-ით და შეიკრიბოს და დაიპრინტოს ჯამი
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

# print(num1 + num2)

# name = "nodo"
# age = 16
# surname = "rusishvili"

# print("hello", name,"your surname is", surname ,"and your age is", age )

name = input("name: " )
surname = input("surname: " )
age = input("age: " )

my_text = "hello {} your surname is {} and your age is {}"
print(my_text.format(name,surname,age))

