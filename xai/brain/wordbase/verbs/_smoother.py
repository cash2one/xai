

from xai.brain.wordbase.verbs._smooth import _SMOOTH

#calss header
class _SMOOTHER(_SMOOTH, ):
	def __init__(self,): 
		_SMOOTH.__init__(self)
		self.name = "SMOOTHER"
		self.specie = 'verbs'
		self.basic = "smooth"
		self.jsondata = {}
