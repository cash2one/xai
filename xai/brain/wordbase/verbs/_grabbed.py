

from xai.brain.wordbase.verbs._grab import _GRAB

#calss header
class _GRABBED(_GRAB, ):
	def __init__(self,): 
		_GRAB.__init__(self)
		self.name = "GRABBED"
		self.specie = 'verbs'
		self.basic = "grab"
		self.jsondata = {}
