

from xai.brain.wordbase.verbs._recruit import _RECRUIT

#calss header
class _RECRUITED(_RECRUIT, ):
	def __init__(self,): 
		_RECRUIT.__init__(self)
		self.name = "RECRUITED"
		self.specie = 'verbs'
		self.basic = "recruit"
		self.jsondata = {}
