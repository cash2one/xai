

from xai.brain.wordbase.verbs._confirm import _CONFIRM

#calss header
class _CONFIRMING(_CONFIRM, ):
	def __init__(self,): 
		_CONFIRM.__init__(self)
		self.name = "CONFIRMING"
		self.specie = 'verbs'
		self.basic = "confirm"
		self.jsondata = {}
