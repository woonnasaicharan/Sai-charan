# Class variables can be accessed using class Name directly

# You can create n number of objects of a class

# Creating class instance variables

# self keyword

# __init__() and arguments

class AC:

    def __init__(self, brand):

        self.brand = brand

    def turn_on(self):

        print(f" {self.brand} Ac turned on")

    def turn_off(self):

        print("Ac turned off")

    def change_temp(self):

        pass

class light:
    watts = 6
    colour ="white"
    brand ="lg"
    shape ="lll"
    
    def __inti__(self):
        print("light turn on")
        
    def turn_off(self):
        print("light turn off")
        
    def intensity(self):
        print("intensity of light ")

class Room:

    def __init__(self, ac):

        self.temp = 24

        self.ac = ac

ac = AC("samsung")
t = light()
print(t.turn_off())
room = Room(ac)
room.ac.turn_on()

 
 
 
 