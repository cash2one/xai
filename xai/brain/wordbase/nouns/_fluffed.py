

from xai.brain.wordbase.nouns._fluff import _FLUFF

#calss header
class _FLUFFED(_FLUFF, ):
	def __init__(self,): 
		_FLUFF.__init__(self)
		self.name = "FLUFFED"
		self.specie = 'nouns'
		self.basic = "fluff"
		self.jsondata = {}
