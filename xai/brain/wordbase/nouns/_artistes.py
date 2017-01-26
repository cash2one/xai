

from xai.brain.wordbase.nouns._artiste import _ARTISTE

#calss header
class _ARTISTES(_ARTISTE, ):
	def __init__(self,): 
		_ARTISTE.__init__(self)
		self.name = "ARTISTES"
		self.specie = 'nouns'
		self.basic = "artiste"
		self.jsondata = {}
