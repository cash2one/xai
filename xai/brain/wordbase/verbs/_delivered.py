

from xai.brain.wordbase.verbs._deliver import _DELIVER

#calss header
class _DELIVERED(_DELIVER, ):
	def __init__(self,): 
		_DELIVER.__init__(self)
		self.name = "DELIVERED"
		self.specie = 'verbs'
		self.basic = "deliver"
		self.jsondata = {}
