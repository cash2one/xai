

from xai.brain.wordbase.nouns._imprint import _IMPRINT

#calss header
class _IMPRINTED(_IMPRINT, ):
	def __init__(self,): 
		_IMPRINT.__init__(self)
		self.name = "IMPRINTED"
		self.specie = 'nouns'
		self.basic = "imprint"
		self.jsondata = {}
