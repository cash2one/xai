

from xai.brain.wordbase.nouns._pharmacy import _PHARMACY

#calss header
class _PHARMACIES(_PHARMACY, ):
	def __init__(self,): 
		_PHARMACY.__init__(self)
		self.name = "PHARMACIES"
		self.specie = 'nouns'
		self.basic = "pharmacy"
		self.jsondata = {}
