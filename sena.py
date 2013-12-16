from random import choice
from random import shuffle

class MegaSena(object):

    def __init__(self):
        self.mix = []
        self.game = []

    def generate_numbers(self, max_number=61):
        self.max_number = max_number
        for x in xrange(1,self.max_number):
            self.mix.append(x)

    def play(self, max_size=6):
        self.max_size = max_size
        for s in xrange(0,self.max_size):
            shuffle(self.mix)
            l = choice(self.mix)
            self.mix.remove(l)
            self.game.append(l)
            
    def show(self):
        self.game.sort()
        print self.game

sena_1 = MegaSena()
sena_1.generate_numbers()
sena_1.play()
sena_1.show()

sena_2 = MegaSena()
sena_2.generate_numbers()
sena_2.play()
sena_2.show()

sena_3 = MegaSena()
sena_3.generate_numbers()
sena_3.play()
sena_3.show()