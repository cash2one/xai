

from xai.brain.wordbase.adjectives._passive import _PASSIVE

#calss header
class _PASSIVES(_PASSIVE, ):
	def __init__(self,): 
		_PASSIVE.__init__(self)
		self.name = "PASSIVES"
		self.specie = 'adjectives'
		self.basic = "passive"
		self.jsondata = {}
