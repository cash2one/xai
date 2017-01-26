

from xai.brain.wordbase.nouns._pharmaceutical import _PHARMACEUTICAL

#calss header
class _PHARMACEUTICALS(_PHARMACEUTICAL, ):
	def __init__(self,): 
		_PHARMACEUTICAL.__init__(self)
		self.name = "PHARMACEUTICALS"
		self.specie = 'nouns'
		self.basic = "pharmaceutical"
		self.jsondata = {}
