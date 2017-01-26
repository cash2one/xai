

from xai.brain.wordbase.adjectives._gentle import _GENTLE

#calss header
class _GENTLER(_GENTLE, ):
	def __init__(self,): 
		_GENTLE.__init__(self)
		self.name = "GENTLER"
		self.specie = 'adjectives'
		self.basic = "gentle"
		self.jsondata = {}
