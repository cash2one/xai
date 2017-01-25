

from xai.brain.wordbase.nouns._irregular import _IRREGULAR

#calss header
class _IRREGULARS(_IRREGULAR, ):
	def __init__(self,): 
		_IRREGULAR.__init__(self)
		self.name = "IRREGULARS"
		self.specie = 'nouns'
		self.basic = "irregular"
		self.jsondata = {}
