

from xai.brain.wordbase.verbs._critique import _CRITIQUE

#calss header
class _CRITIQUED(_CRITIQUE, ):
	def __init__(self,): 
		_CRITIQUE.__init__(self)
		self.name = "CRITIQUED"
		self.specie = 'verbs'
		self.basic = "critique"
		self.jsondata = {}
