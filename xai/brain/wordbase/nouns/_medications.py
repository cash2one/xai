

from xai.brain.wordbase.nouns._medication import _MEDICATION

#calss header
class _MEDICATIONS(_MEDICATION, ):
	def __init__(self,): 
		_MEDICATION.__init__(self)
		self.name = "MEDICATIONS"
		self.specie = 'nouns'
		self.basic = "medication"
		self.jsondata = {}
