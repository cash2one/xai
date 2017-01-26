

from xai.brain.wordbase.adjectives._postgraduate import _POSTGRADUATE

#calss header
class _POSTGRADUATES(_POSTGRADUATE, ):
	def __init__(self,): 
		_POSTGRADUATE.__init__(self)
		self.name = "POSTGRADUATES"
		self.specie = 'adjectives'
		self.basic = "postgraduate"
		self.jsondata = {}
