

from xai.brain.wordbase.verbs._worsen import _WORSEN

#calss header
class _WORSENED(_WORSEN, ):
	def __init__(self,): 
		_WORSEN.__init__(self)
		self.name = "WORSENED"
		self.specie = 'verbs'
		self.basic = "worsen"
		self.jsondata = {}
