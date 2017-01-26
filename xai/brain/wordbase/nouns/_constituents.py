

from xai.brain.wordbase.nouns._constituent import _CONSTITUENT

#calss header
class _CONSTITUENTS(_CONSTITUENT, ):
	def __init__(self,): 
		_CONSTITUENT.__init__(self)
		self.name = "CONSTITUENTS"
		self.specie = 'nouns'
		self.basic = "constituent"
		self.jsondata = {}
