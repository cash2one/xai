

from xai.brain.wordbase.nouns._signpost import _SIGNPOST

#calss header
class _SIGNPOSTED(_SIGNPOST, ):
	def __init__(self,): 
		_SIGNPOST.__init__(self)
		self.name = "SIGNPOSTED"
		self.specie = 'nouns'
		self.basic = "signpost"
		self.jsondata = {}
