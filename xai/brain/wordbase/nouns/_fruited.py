

from xai.brain.wordbase.nouns._fruit import _FRUIT

#calss header
class _FRUITED(_FRUIT, ):
	def __init__(self,): 
		_FRUIT.__init__(self)
		self.name = "FRUITED"
		self.specie = 'nouns'
		self.basic = "fruit"
		self.jsondata = {}
