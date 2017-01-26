

from xai.brain.wordbase.verbs._steer import _STEER

#calss header
class _STEERED(_STEER, ):
	def __init__(self,): 
		_STEER.__init__(self)
		self.name = "STEERED"
		self.specie = 'verbs'
		self.basic = "steer"
		self.jsondata = {}
