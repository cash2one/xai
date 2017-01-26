

from xai.brain.wordbase.nouns._insurance import _INSURANCE

#calss header
class _INSURANCES(_INSURANCE, ):
	def __init__(self,): 
		_INSURANCE.__init__(self)
		self.name = "INSURANCES"
		self.specie = 'nouns'
		self.basic = "insurance"
		self.jsondata = {}
