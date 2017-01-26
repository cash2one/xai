

from xai.brain.wordbase.verbs._delegate import _DELEGATE

#calss header
class _DELEGATED(_DELEGATE, ):
	def __init__(self,): 
		_DELEGATE.__init__(self)
		self.name = "DELEGATED"
		self.specie = 'verbs'
		self.basic = "delegate"
		self.jsondata = {}
