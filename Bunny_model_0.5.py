import random as rnd

class Individual:
    def __init__(self):
        self.age = 0
        self.resources = 10
        self.max_age = rnd.randint(5,10)
    
    def get_older(self):
        self.age += 1
        self.resources -= 3
        
    def search_food(self):
        chance_to_find_food = 0.3
        if rnd.random() < chance_to_find_food:
            n_carrots = rnd.randint(5,10)
            self.eat(n_carrots)        
        
    def eat(self,n_carrots):
        self.resources += n_carrots
        
bunny = Individual()

maxtime = 10

for t in range(maxtime):
    bunny.get_older()
    bunny.search_food()
    if bunny.age > bunny.max_age:
        print 'A bunny died of old age'
        break    
    elif bunny.resources < 0:
        print 'A bunny died of starvation'
        break
    
print bunny.resources, bunny.age      
        
        