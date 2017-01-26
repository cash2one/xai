

from xai.brain.wordbase.nouns._weapon import _WEAPON

#calss header
class _WEAPONS(_WEAPON, ):
	def __init__(self,): 
		_WEAPON.__init__(self)
		self.name = "WEAPONS"
		self.specie = 'nouns'
		self.basic = "weapon"
		self.jsondata = {}
