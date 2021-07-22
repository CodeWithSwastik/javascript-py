from javascript import *
console.clear(0)

class FalseDev:
    def __init__(self):
        self.age = 17
        self.skills = 'Pro'
    
try:
    lmao = 1/0
except Exception as err:
    console.error(err, verbose=True)