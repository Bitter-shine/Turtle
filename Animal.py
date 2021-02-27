import random
class Animal():
    def seeanimal(self):
        n = random.randint(1,5)
        if n == 1:
            m = "吃饭"
        elif n == 2:
            m = "喝奶"
        elif n == 3:
            m = "玩耍"
        elif n == 4:
            m = "睡觉"
        else:
            m = "运动"
        print(f"{name}正在{m}")
    def animalmood(self):
        mood = random.randint(1, 5)
        if mood == 1:
            m = "很高兴"
        elif mood == 2:
            m = "愁眉苦脸"
        elif mood == 3:
            m = "开怀大笑"
        elif mood == 4:
            m = "很疑惑"
        else:
            m = "很失望"
        print(f"{name}{m}")
a = Animal()
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