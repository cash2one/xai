

from xai.brain.wordbase.nouns._contestant import _CONTESTANT

#calss header
class _CONTESTANTS(_CONTESTANT, ):
	def __init__(self,): 
		_CONTESTANT.__init__(self)
		self.name = "CONTESTANTS"
		self.specie = 'nouns'
		self.basic = "contestant"
		self.jsondata = {}
