

from xai.brain.wordbase.adjectives._lonely import _LONELY

#calss header
class _LONELIER(_LONELY, ):
	def __init__(self,): 
		_LONELY.__init__(self)
		self.name = "LONELIER"
		self.specie = 'adjectives'
		self.basic = "lonely"
		self.jsondata = {}
