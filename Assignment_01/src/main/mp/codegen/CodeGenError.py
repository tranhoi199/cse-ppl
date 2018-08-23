class IllegalOperandException(Exception):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "Illegal Operand: " + self.s +"\n"
class IllegalRuntimeException(Exception):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "Illegal Runtime: " + self.s +"\n"