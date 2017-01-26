

from xai.brain.wordbase.adverbs._clean import _CLEAN

#calss header
class _CLEANED(_CLEAN, ):
	def __init__(self,): 
		_CLEAN.__init__(self)
		self.name = "CLEANED"
		self.specie = 'adverbs'
		self.basic = "clean"
		self.jsondata = {}
