

from xai.brain.wordbase.verbs._transmit import _TRANSMIT

#calss header
class _TRANSMITTED(_TRANSMIT, ):
	def __init__(self,): 
		_TRANSMIT.__init__(self)
		self.name = "TRANSMITTED"
		self.specie = 'verbs'
		self.basic = "transmit"
		self.jsondata = {}
