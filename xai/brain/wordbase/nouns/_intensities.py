

from xai.brain.wordbase.nouns._intensity import _INTENSITY

#calss header
class _INTENSITIES(_INTENSITY, ):
	def __init__(self,): 
		_INTENSITY.__init__(self)
		self.name = "INTENSITIES"
		self.specie = 'nouns'
		self.basic = "intensity"
		self.jsondata = {}
