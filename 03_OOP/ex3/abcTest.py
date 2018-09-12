from abc import ABC

class AbstractClass(ABC):
    def say(self, msg):
        print(msg)

a = AbstractClass()
a.say('123')