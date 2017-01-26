

from xai.brain.wordbase.verbs._deactivate import _DEACTIVATE

#calss header
class _DEACTIVATED(_DEACTIVATE, ):
	def __init__(self,): 
		_DEACTIVATE.__init__(self)
		self.name = "DEACTIVATED"
		self.specie = 'verbs'
		self.basic = "deactivate"
		self.jsondata = {}
