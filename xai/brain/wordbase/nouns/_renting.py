

from xai.brain.wordbase.nouns._rent import _RENT

#calss header
class _RENTING(_RENT, ):
	def __init__(self,): 
		_RENT.__init__(self)
		self.name = "RENTING"
		self.specie = 'nouns'
		self.basic = "rent"
		self.jsondata = {}
