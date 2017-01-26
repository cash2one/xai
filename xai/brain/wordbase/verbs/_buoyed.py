

from xai.brain.wordbase.verbs._buoy import _BUOY

#calss header
class _BUOYED(_BUOY, ):
	def __init__(self,): 
		_BUOY.__init__(self)
		self.name = "BUOYED"
		self.specie = 'verbs'
		self.basic = "buoy"
		self.jsondata = {}
