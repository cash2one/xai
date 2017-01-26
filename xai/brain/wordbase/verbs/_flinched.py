

from xai.brain.wordbase.verbs._flinch import _FLINCH

#calss header
class _FLINCHED(_FLINCH, ):
	def __init__(self,): 
		_FLINCH.__init__(self)
		self.name = "FLINCHED"
		self.specie = 'verbs'
		self.basic = "flinch"
		self.jsondata = {}
