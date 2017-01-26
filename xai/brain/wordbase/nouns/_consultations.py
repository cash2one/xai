

from xai.brain.wordbase.nouns._consultation import _CONSULTATION

#calss header
class _CONSULTATIONS(_CONSULTATION, ):
	def __init__(self,): 
		_CONSULTATION.__init__(self)
		self.name = "CONSULTATIONS"
		self.specie = 'nouns'
		self.basic = "consultation"
		self.jsondata = {}
