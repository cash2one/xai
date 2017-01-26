

from xai.brain.wordbase.nouns._poison import _POISON

#calss header
class _POISONED(_POISON, ):
	def __init__(self,): 
		_POISON.__init__(self)
		self.name = "POISONED"
		self.specie = 'nouns'
		self.basic = "poison"
		self.jsondata = {}
