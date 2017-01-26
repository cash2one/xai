

from xai.brain.wordbase.adjectives._smooth import _SMOOTH

#calss header
class _SMOOTHED(_SMOOTH, ):
	def __init__(self,): 
		_SMOOTH.__init__(self)
		self.name = "SMOOTHED"
		self.specie = 'adjectives'
		self.basic = "smooth"
		self.jsondata = {}
