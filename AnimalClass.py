class Animal():
    def __init__(self):
        food = "Anything"
        hunger = True
    def eat(self):
        self.hunger = false
        print("Голод утолён")
    def sleep(self):
        self.hunger = true
        print("Животное поспало, оно голодно")
    def makeNoise(self, noise):
        print(noise)
