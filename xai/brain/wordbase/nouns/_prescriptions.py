

from xai.brain.wordbase.nouns._prescription import _PRESCRIPTION

#calss header
class _PRESCRIPTIONS(_PRESCRIPTION, ):
	def __init__(self,): 
		_PRESCRIPTION.__init__(self)
		self.name = "PRESCRIPTIONS"
		self.specie = 'nouns'
		self.basic = "prescription"
		self.jsondata = {}
