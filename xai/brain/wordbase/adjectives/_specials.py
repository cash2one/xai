

from xai.brain.wordbase.adjectives._special import _SPECIAL

#calss header
class _SPECIALS(_SPECIAL, ):
	def __init__(self,): 
		_SPECIAL.__init__(self)
		self.name = "SPECIALS"
		self.specie = 'adjectives'
		self.basic = "special"
		self.jsondata = {}
