

from xai.brain.wordbase.verbs._betray import _BETRAY

#calss header
class _BETRAYED(_BETRAY, ):
	def __init__(self,): 
		_BETRAY.__init__(self)
		self.name = "BETRAYED"
		self.specie = 'verbs'
		self.basic = "betray"
		self.jsondata = {}
