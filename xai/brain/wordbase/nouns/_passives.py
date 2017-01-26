

from xai.brain.wordbase.nouns._passive import _PASSIVE

#calss header
class _PASSIVES(_PASSIVE, ):
	def __init__(self,): 
		_PASSIVE.__init__(self)
		self.name = "PASSIVES"
		self.specie = 'nouns'
		self.basic = "passive"
		self.jsondata = {}
