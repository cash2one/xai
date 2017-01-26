

from xai.brain.wordbase.nouns._buoy import _BUOY

#calss header
class _BUOYED(_BUOY, ):
	def __init__(self,): 
		_BUOY.__init__(self)
		self.name = "BUOYED"
		self.specie = 'nouns'
		self.basic = "buoy"
		self.jsondata = {}
