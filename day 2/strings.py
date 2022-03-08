name = "nodo"
#რეალურად ყველა სტრინგი შეგვიძლია მივიჩნიოთ 
#char ტიპის ელემენტებისგან შემდგარ სიად

#შეგვიძლია დავპრინტოთ მეორე ასო სტრინგში
print(name[1])

#შეგვიძლია დავთვალოთ სტრინგის სიგრძე
print(len(name))

#შევამოწმოთ რაიმე ელემენტის არსებობა მოცემულ სტრინგში
print("l" in name)

#slicing
surname = "rusishvili"
print(surname[2:5])

print(surname[:5])
print(name[5:])

#negative indexes
print(surname[-1])
print(surname[-6])