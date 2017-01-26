

from xai.brain.wordbase.nouns._brat import _BRAT

#calss header
class _BRATS(_BRAT, ):
	def __init__(self,): 
		_BRAT.__init__(self)
		self.name = "BRATS"
		self.specie = 'nouns'
		self.basic = "brat"
		self.jsondata = {}
