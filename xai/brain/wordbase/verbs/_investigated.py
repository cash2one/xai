

from xai.brain.wordbase.verbs._investigate import _INVESTIGATE

#calss header
class _INVESTIGATED(_INVESTIGATE, ):
	def __init__(self,): 
		_INVESTIGATE.__init__(self)
		self.name = "INVESTIGATED"
		self.specie = 'verbs'
		self.basic = "investigate"
		self.jsondata = {}
