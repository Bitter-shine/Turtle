import random
class number(object):
    def __init__(self,name,school):
        self.name = name
        self.school = school
    def say(self):
        print(f"Your are number 00{self.name},in school {self.school}.")
n = number(random.randint(1,10),random.randint(1,10))
n.say()