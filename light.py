class light:
    watts = 6
    colour ="white"
    brand ="lg"
    shape ="lll"
    
    def turn_on(self):
        print("light turn on")
        
    def turn_off(self):
        print("light turn off")
        
    def intensity(self):
        print("intensity of light ")

t = light()
print(t.turn_off())
