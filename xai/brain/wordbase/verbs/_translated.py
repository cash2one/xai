

from xai.brain.wordbase.verbs._translate import _TRANSLATE

#calss header
class _TRANSLATED(_TRANSLATE, ):
	def __init__(self,): 
		_TRANSLATE.__init__(self)
		self.name = "TRANSLATED"
		self.specie = 'verbs'
		self.basic = "translate"
		self.jsondata = {}
