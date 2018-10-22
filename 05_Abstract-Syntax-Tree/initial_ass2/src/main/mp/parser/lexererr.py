
class ErrorToken(Exception):
    def __init__(self,s):
        self.message = "Error Token "+ s

class UncloseString(Exception):
    def __init__(self,s):
        self.message = "Unclosed String: "+ s

class IllegalEscape(Exception):
    def __init__(self,s):
        self.message = "Illegal Escape In String: "+ s



