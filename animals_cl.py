class Animals:
    tip = "Хордовые"
    podvid = "Позвоночные"
    klas = "Млекопитающие"
    def info_ani(self):
        return print("\nТип:",self.tip,"\nПодвид:",self.podvid,"\nКласс:",self.klas)
class Mammals(Animals):
        def __init__(self, otryad, semeystvo, vid):
            self.otryad = otryad
            self.semeystvo = semeystvo
            self.vid = vid
        
class Dog(Mammals):
    def __init__(self,clichka_dog):
        self.clichka_dog = clichka_dog
class Cat(Mammals):
    def __init__(self,clichka_cat):
        self.clichka_dog = clichka_cat
class Human(Mammals):
    def __init__(self,name):
        self.name = name 
        
   
mamm_hum = Mammals("Приматы", "Люди", "Человек разумный")    
its_me = Human("Егор")
its_me.info_ani()
print("Отряд:",mamm_hum.otryad,"\nСемейство:",mamm_hum.semeystvo,"\nВид:",mamm_hum.vid,"\nИмя:",its_me.name)
