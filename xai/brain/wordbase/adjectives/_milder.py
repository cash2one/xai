

from xai.brain.wordbase.adjectives._mild import _MILD

#calss header
class _MILDER(_MILD, ):
	def __init__(self,): 
		_MILD.__init__(self)
		self.name = "MILDER"
		self.specie = 'adjectives'
		self.basic = "mild"
		self.jsondata = {}
