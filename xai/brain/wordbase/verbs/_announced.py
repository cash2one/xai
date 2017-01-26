

from xai.brain.wordbase.verbs._announce import _ANNOUNCE

#calss header
class _ANNOUNCED(_ANNOUNCE, ):
	def __init__(self,): 
		_ANNOUNCE.__init__(self)
		self.name = "ANNOUNCED"
		self.specie = 'verbs'
		self.basic = "announce"
		self.jsondata = {}
