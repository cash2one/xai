

from xai.brain.wordbase.verbs._loan import _LOAN

#calss header
class _LOANED(_LOAN, ):
	def __init__(self,): 
		_LOAN.__init__(self)
		self.name = "LOANED"
		self.specie = 'verbs'
		self.basic = "loan"
		self.jsondata = {}
