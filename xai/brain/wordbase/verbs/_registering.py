

from xai.brain.wordbase.verbs._register import _REGISTER

#calss header
class _REGISTERING(_REGISTER, ):
	def __init__(self,): 
		_REGISTER.__init__(self)
		self.name = "REGISTERING"
		self.specie = 'verbs'
		self.basic = "register"
		self.jsondata = {}
