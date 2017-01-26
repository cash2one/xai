

from xai.brain.wordbase.nouns._compound import _COMPOUND

#calss header
class _COMPOUNDED(_COMPOUND, ):
	def __init__(self,): 
		_COMPOUND.__init__(self)
		self.name = "COMPOUNDED"
		self.specie = 'nouns'
		self.basic = "compound"
		self.jsondata = {}
