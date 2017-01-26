

from xai.brain.wordbase.verbs._greet import _GREET

#calss header
class _GREETS(_GREET, ):
	def __init__(self,): 
		_GREET.__init__(self)
		self.name = "GREETS"
		self.specie = 'verbs'
		self.basic = "greet"
		self.jsondata = {}
