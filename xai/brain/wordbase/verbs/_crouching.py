

from xai.brain.wordbase.verbs._crouch import _CROUCH

#calss header
class _CROUCHING(_CROUCH, ):
	def __init__(self,): 
		_CROUCH.__init__(self)
		self.name = "CROUCHING"
		self.specie = 'verbs'
		self.basic = "crouch"
		self.jsondata = {}
