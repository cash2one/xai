

from xai.brain.wordbase.verbs._worsen import _WORSEN

#calss header
class _WORSENING(_WORSEN, ):
	def __init__(self,): 
		_WORSEN.__init__(self)
		self.name = "WORSENING"
		self.specie = 'verbs'
		self.basic = "worsen"
		self.jsondata = {}
