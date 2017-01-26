

from xai.brain.wordbase.adjectives._sedate import _SEDATE

#calss header
class _SEDATED(_SEDATE, ):
	def __init__(self,): 
		_SEDATE.__init__(self)
		self.name = "SEDATED"
		self.specie = 'adjectives'
		self.basic = "sedate"
		self.jsondata = {}
