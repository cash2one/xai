

from xai.brain.wordbase.verbs._volunteer import _VOLUNTEER

#calss header
class _VOLUNTEERS(_VOLUNTEER, ):
	def __init__(self,): 
		_VOLUNTEER.__init__(self)
		self.name = "VOLUNTEERS"
		self.specie = 'verbs'
		self.basic = "volunteer"
		self.jsondata = {}
