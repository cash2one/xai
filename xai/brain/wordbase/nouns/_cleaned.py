

from xai.brain.wordbase.nouns._clean import _CLEAN

#calss header
class _CLEANED(_CLEAN, ):
	def __init__(self,): 
		_CLEAN.__init__(self)
		self.name = "CLEANED"
		self.specie = 'nouns'
		self.basic = "clean"
		self.jsondata = {}
