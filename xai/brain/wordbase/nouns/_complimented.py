

from xai.brain.wordbase.nouns._compliment import _COMPLIMENT

#calss header
class _COMPLIMENTED(_COMPLIMENT, ):
	def __init__(self,): 
		_COMPLIMENT.__init__(self)
		self.name = "COMPLIMENTED"
		self.specie = 'nouns'
		self.basic = "compliment"
		self.jsondata = {}
