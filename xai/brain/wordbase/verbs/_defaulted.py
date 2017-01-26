

from xai.brain.wordbase.verbs._default import _DEFAULT

#calss header
class _DEFAULTED(_DEFAULT, ):
	def __init__(self,): 
		_DEFAULT.__init__(self)
		self.name = "DEFAULTED"
		self.specie = 'verbs'
		self.basic = "default"
		self.jsondata = {}
