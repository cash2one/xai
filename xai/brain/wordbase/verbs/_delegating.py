

from xai.brain.wordbase.verbs._delegate import _DELEGATE

#calss header
class _DELEGATING(_DELEGATE, ):
	def __init__(self,): 
		_DELEGATE.__init__(self)
		self.name = "DELEGATING"
		self.specie = 'verbs'
		self.basic = "delegate"
		self.jsondata = {}
