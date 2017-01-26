

from xai.brain.wordbase.verbs._compliment import _COMPLIMENT

#calss header
class _COMPLIMENTED(_COMPLIMENT, ):
	def __init__(self,): 
		_COMPLIMENT.__init__(self)
		self.name = "COMPLIMENTED"
		self.specie = 'verbs'
		self.basic = "compliment"
		self.jsondata = {}
