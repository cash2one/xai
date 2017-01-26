

from xai.brain.wordbase.verbs._erode import _ERODE

#calss header
class _ERODED(_ERODE, ):
	def __init__(self,): 
		_ERODE.__init__(self)
		self.name = "ERODED"
		self.specie = 'verbs'
		self.basic = "erode"
		self.jsondata = {}
