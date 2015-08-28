class Individual:
    def __init__(self):
        self.age = 0
        self.resources = 10
    
    def get_older(self):
        self.age += 1
        
        
bunny = Individual()

bunny.get_older()

bunny.age += 1

print bunny.age        
        
        