

from xai.brain.wordbase.verbs._shift import _SHIFT

#calss header
class _SHIFTED(_SHIFT, ):
	def __init__(self,): 
		_SHIFT.__init__(self)
		self.name = "SHIFTED"
		self.specie = 'verbs'
		self.basic = "shift"
		self.jsondata = {}
