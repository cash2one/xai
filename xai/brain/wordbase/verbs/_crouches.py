

from xai.brain.wordbase.verbs._crouch import _CROUCH

#calss header
class _CROUCHES(_CROUCH, ):
	def __init__(self,): 
		_CROUCH.__init__(self)
		self.name = "CROUCHES"
		self.specie = 'verbs'
		self.basic = "crouch"
		self.jsondata = {}
