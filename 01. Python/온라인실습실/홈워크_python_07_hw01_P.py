class Doggy:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def bark(cls):
        print('멍멍')



shiro = Doggy('shiro', 'jindo')
print(shiro)       
