

from xai.brain.wordbase.verbs._foul import _FOUL

#calss header
class _FOULING(_FOUL, ):
	def __init__(self,): 
		_FOUL.__init__(self)
		self.name = "FOULING"
		self.specie = 'verbs'
		self.basic = "foul"
		self.jsondata = {}
