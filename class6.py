"""class Parrot:

    # class atrribute
    species="bird"
    
    # instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot("blu",10)
woo=Parrot("woo",15)
print("blu is a {}".format(blu.species))
print("woo is also a{}".format(woo.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))"""
class Parrot:
    
    # instance attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return"{} sings {}".format(self.name,song)
    
    def dance(self):
        return"{} is now dancing".format(self.name)
blu=Parrot("blu",10)
print(blu.sing("Happy"))
print(blu.dance())

