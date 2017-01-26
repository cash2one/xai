

from xai.brain.wordbase.nouns._supplement import _SUPPLEMENT

#calss header
class _SUPPLEMENTED(_SUPPLEMENT, ):
	def __init__(self,): 
		_SUPPLEMENT.__init__(self)
		self.name = "SUPPLEMENTED"
		self.specie = 'nouns'
		self.basic = "supplement"
		self.jsondata = {}
