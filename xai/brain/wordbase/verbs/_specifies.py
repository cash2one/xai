

from xai.brain.wordbase.verbs._specify import _SPECIFY

#calss header
class _SPECIFIES(_SPECIFY, ):
	def __init__(self,): 
		_SPECIFY.__init__(self)
		self.name = "SPECIFIES"
		self.specie = 'verbs'
		self.basic = "specify"
		self.jsondata = {}
