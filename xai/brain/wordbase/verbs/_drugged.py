

from xai.brain.wordbase.verbs._drug import _DRUG

#calss header
class _DRUGGED(_DRUG, ):
	def __init__(self,): 
		_DRUG.__init__(self)
		self.name = "DRUGGED"
		self.specie = 'verbs'
		self.basic = "drug"
		self.jsondata = {}
