

from xai.brain.wordbase.verbs._halt import _HALT

#calss header
class _HALTED(_HALT, ):
	def __init__(self,): 
		_HALT.__init__(self)
		self.name = "HALTED"
		self.specie = 'verbs'
		self.basic = "halt"
		self.jsondata = {}
