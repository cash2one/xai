

from xai.brain.wordbase.nouns._misprint import _MISPRINT

#calss header
class _MISPRINTED(_MISPRINT, ):
	def __init__(self,): 
		_MISPRINT.__init__(self)
		self.name = "MISPRINTED"
		self.specie = 'nouns'
		self.basic = "misprint"
		self.jsondata = {}
