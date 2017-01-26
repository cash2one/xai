

from xai.brain.wordbase.adjectives._polite import _POLITE

#calss header
class _POLITEST(_POLITE, ):
	def __init__(self,): 
		_POLITE.__init__(self)
		self.name = "POLITEST"
		self.specie = 'adjectives'
		self.basic = "polite"
		self.jsondata = {}
