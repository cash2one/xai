

from xai.brain.wordbase.nouns._emergency import _EMERGENCY

#calss header
class _EMERGENCIES(_EMERGENCY, ):
	def __init__(self,): 
		_EMERGENCY.__init__(self)
		self.name = "EMERGENCIES"
		self.specie = 'nouns'
		self.basic = "emergency"
		self.jsondata = {}
