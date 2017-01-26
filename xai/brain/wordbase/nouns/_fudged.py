

from xai.brain.wordbase.nouns._fudge import _FUDGE

#calss header
class _FUDGED(_FUDGE, ):
	def __init__(self,): 
		_FUDGE.__init__(self)
		self.name = "FUDGED"
		self.specie = 'nouns'
		self.basic = "fudge"
		self.jsondata = {}
