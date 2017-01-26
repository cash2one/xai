

from xai.brain.wordbase.verbs._classify import _CLASSIFY

#calss header
class _CLASSIFIES(_CLASSIFY, ):
	def __init__(self,): 
		_CLASSIFY.__init__(self)
		self.name = "CLASSIFIES"
		self.specie = 'verbs'
		self.basic = "classify"
		self.jsondata = {}
