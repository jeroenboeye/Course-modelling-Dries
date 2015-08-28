class Individual:
    def __init__(self):
        self.age = 0
        self.resources = 10
    
    def get_older(self):
        self.age += 1
        self.resources -= 3
        
    def eat(self,n_carrots):
        self.resources += n_carrots
        
bunny = Individual()

maxtime = 10

for t in range(maxtime):
    bunny.get_older()
    bunny.eat(5)
    
print bunny.resources, bunny.age      
        
        