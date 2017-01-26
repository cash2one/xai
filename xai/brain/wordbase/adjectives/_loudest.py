

from xai.brain.wordbase.adjectives._loud import _LOUD

#calss header
class _LOUDEST(_LOUD, ):
	def __init__(self,): 
		_LOUD.__init__(self)
		self.name = "LOUDEST"
		self.specie = 'adjectives'
		self.basic = "loud"
		self.jsondata = {}
