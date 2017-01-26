

from xai.brain.wordbase.verbs._deafen import _DEAFEN

#calss header
class _DEAFENED(_DEAFEN, ):
	def __init__(self,): 
		_DEAFEN.__init__(self)
		self.name = "DEAFENED"
		self.specie = 'verbs'
		self.basic = "deafen"
		self.jsondata = {}
