

from xai.brain.wordbase.verbs._pierce import _PIERCE

#calss header
class _PIERCED(_PIERCE, ):
	def __init__(self,): 
		_PIERCE.__init__(self)
		self.name = "PIERCED"
		self.specie = 'verbs'
		self.basic = "pierce"
		self.jsondata = {}
