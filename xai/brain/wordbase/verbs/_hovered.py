

from xai.brain.wordbase.verbs._hover import _HOVER

#calss header
class _HOVERED(_HOVER, ):
	def __init__(self,): 
		_HOVER.__init__(self)
		self.name = "HOVERED"
		self.specie = 'verbs'
		self.basic = "hover"
		self.jsondata = {}
