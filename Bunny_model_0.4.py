class Individual:
    def __init__(self):
        self.age = 0
        self.resources = 10
    
    def get_older(self):
        self.age += 1
        
    def eat(self,n_carrots):
        self.resources += n_carrots
        
bunny = Individual()

bunny.eat(5)
    
print bunny.resources   
        
        