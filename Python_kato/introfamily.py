import myself

class IntroFam(myself.Intro):
    def __init__(self, name, age, cat):
        super().__init__(name, age)
        self.cat = cat

    def cat_out(self):
        print("飼い猫の名前は、" + self.cat + "です")