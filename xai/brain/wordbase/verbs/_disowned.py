

from xai.brain.wordbase.verbs._disown import _DISOWN

#calss header
class _DISOWNED(_DISOWN, ):
	def __init__(self,): 
		_DISOWN.__init__(self)
		self.name = "DISOWNED"
		self.specie = 'verbs'
		self.basic = "disown"
		self.jsondata = {}
