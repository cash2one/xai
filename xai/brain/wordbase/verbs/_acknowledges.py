

from xai.brain.wordbase.verbs._acknowledge import _ACKNOWLEDGE

#calss header
class _ACKNOWLEDGES(_ACKNOWLEDGE, ):
	def __init__(self,): 
		_ACKNOWLEDGE.__init__(self)
		self.name = "ACKNOWLEDGES"
		self.specie = 'verbs'
		self.basic = "acknowledge"
		self.jsondata = {}
