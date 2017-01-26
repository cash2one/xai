

from xai.brain.wordbase.verbs._greet import _GREET

#calss header
class _GREETED(_GREET, ):
	def __init__(self,): 
		_GREET.__init__(self)
		self.name = "GREETED"
		self.specie = 'verbs'
		self.basic = "greet"
		self.jsondata = {}
