# File created by : Zydaan Khan

# welcome to classes...

# create three more lizards....
# add attributes
# add a method...

class Lizard:
    def __init__(self, name):
        # self.name = "Fred"
        self.name = name
        self.species = "Lizard"
        self.coldblooded = True
    def jump(self):
        print(self.name + " has jumped...")
    def eat(self):
        print(self.name + " is eating....")


my_lizard = Lizard("Fred", "Iguana")
his_lizard = Lizard("Doug", "Basilisk")
flying_lizard = Lizard("Homelander", "Draco")

print(my_lizard.name + " is an " + my_lizard.species)
my_lizard.jump()

geckos = []

for i in range(0,5):
    l = Lizard("generic", "gecko")
    # geckos.append(i)
    # geckos.append(l.species)
    geckos.append(l)

print(geckos)

for i in geckos:
    print(geckos[0].jump())






# extra credit...
class Iguana(Lizard):
    def __init__(self, name, species, genus):
        Lizard.__init__(self, name, species)
        self.genus = genus