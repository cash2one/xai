

from xai.brain.wordbase.nouns._sensitivity import _SENSITIVITY

#calss header
class _SENSITIVITIES(_SENSITIVITY, ):
	def __init__(self,): 
		_SENSITIVITY.__init__(self)
		self.name = "SENSITIVITIES"
		self.specie = 'nouns'
		self.basic = "sensitivity"
		self.jsondata = {}
