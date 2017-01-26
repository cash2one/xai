

from xai.brain.wordbase.nouns._beam import _BEAM

#calss header
class _BEAMED(_BEAM, ):
	def __init__(self,): 
		_BEAM.__init__(self)
		self.name = "BEAMED"
		self.specie = 'nouns'
		self.basic = "beam"
		self.jsondata = {}
