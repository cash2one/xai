

from xai.brain.wordbase.verbs._dismiss import _DISMISS

#calss header
class _DISMISSED(_DISMISS, ):
	def __init__(self,): 
		_DISMISS.__init__(self)
		self.name = "DISMISSED"
		self.specie = 'verbs'
		self.basic = "dismiss"
		self.jsondata = {}
