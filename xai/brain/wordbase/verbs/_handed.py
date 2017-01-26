

from xai.brain.wordbase.verbs._hand import _HAND

#calss header
class _HANDED(_HAND, ):
	def __init__(self,): 
		_HAND.__init__(self)
		self.name = "HANDED"
		self.specie = 'verbs'
		self.basic = "hand"
		self.jsondata = {}
