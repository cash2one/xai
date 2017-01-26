

from xai.brain.wordbase.adjectives._frequent import _FREQUENT

#calss header
class _FREQUENTER(_FREQUENT, ):
	def __init__(self,): 
		_FREQUENT.__init__(self)
		self.name = "FREQUENTER"
		self.specie = 'adjectives'
		self.basic = "frequent"
		self.jsondata = {}
