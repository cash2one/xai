

from xai.brain.wordbase.nouns._guesstimate import _GUESSTIMATE

#calss header
class _GUESSTIMATED(_GUESSTIMATE, ):
	def __init__(self,): 
		_GUESSTIMATE.__init__(self)
		self.name = "GUESSTIMATED"
		self.specie = 'nouns'
		self.basic = "guesstimate"
		self.jsondata = {}
