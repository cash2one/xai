

from xai.brain.wordbase.adjectives._medical import _MEDICAL

#calss header
class _MEDICALS(_MEDICAL, ):
	def __init__(self,): 
		_MEDICAL.__init__(self)
		self.name = "MEDICALS"
		self.specie = 'adjectives'
		self.basic = "medical"
		self.jsondata = {}
