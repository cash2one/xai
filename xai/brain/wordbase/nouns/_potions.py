

from xai.brain.wordbase.nouns._potion import _POTION

#calss header
class _POTIONS(_POTION, ):
	def __init__(self,): 
		_POTION.__init__(self)
		self.name = "POTIONS"
		self.specie = 'nouns'
		self.basic = "potion"
		self.jsondata = {}
