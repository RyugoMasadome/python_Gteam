import sys
args = sys.argv

class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def intropre(self):
        print("私の名前は、" + self.name + "です")
        print("年齢は" + self.age + "歳です")


my_self = Intro(args[1], args[2])
