

from xai.brain.wordbase.nouns._medical import _MEDICAL

#calss header
class _MEDICALS(_MEDICAL, ):
	def __init__(self,): 
		_MEDICAL.__init__(self)
		self.name = "MEDICALS"
		self.specie = 'nouns'
		self.basic = "medical"
		self.jsondata = {}
