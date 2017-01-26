

from xai.brain.wordbase.adjectives._heavy import _HEAVY

#calss header
class _HEAVIER(_HEAVY, ):
	def __init__(self,): 
		_HEAVY.__init__(self)
		self.name = "HEAVIER"
		self.specie = 'adjectives'
		self.basic = "heavy"
		self.jsondata = {}
