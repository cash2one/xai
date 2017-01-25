

from xai.brain.wordbase.verbs._follow import _FOLLOW

#calss header
class _FOLLOWED(_FOLLOW, ):
	def __init__(self,): 
		_FOLLOW.__init__(self)
		self.name = "FOLLOWED"
		self.specie = 'verbs'
		self.basic = "follow"
		self.jsondata = {}
