

from xai.brain.wordbase.verbs._underexpose import _UNDEREXPOSE

#calss header
class _UNDEREXPOSED(_UNDEREXPOSE, ):
	def __init__(self,): 
		_UNDEREXPOSE.__init__(self)
		self.name = "UNDEREXPOSED"
		self.specie = 'verbs'
		self.basic = "underexpose"
		self.jsondata = {}
