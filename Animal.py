import random
class Animal():
    def seeanimal(self):
        n = random.randint(1,5)
        if n == 1:
            m = "eating🍔"
        elif n == 2:
            m = "drinking"
        elif n == 3:
            m = "playing"
        elif n == 4:
            m = "sleeping😪"
        else:
            m = "is excreting💩"
        print(f"{name} is {m}")
    def animalmood(self):
        mood = random.randint(1, 5)
        if mood == 1:
            m = " is happy😄"
        elif mood == 2:
            m = " is bad😞"
        elif mood == 3:
            m = " is tired"
        elif mood == 4:
            m = " is doubt"
        else:
            m = " is angry😠"
        print(f"{name}{m}")
a = Animal()
print("******** Animal Home ********")
print("1.Use a.see to look animal's doing.")
print("2.Use a.name to change your animal's name.")
print("3.Use a.mood to see animal's mood.")
print("4.Use quit end the file.")
name = input("Your animal name:")
Animal()
while True:
    i = input(str(">>>"))
    if i == "a.see":
        a.seeanimal()
    elif i == "a.name":
        name = input("Your animal name:")
        Animal()
    elif i == "a.mood":
        a.animalmood()
    elif i == "quit":
        break
    else:
        print("Error:invalid syntax")
