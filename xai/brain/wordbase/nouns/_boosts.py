

from xai.brain.wordbase.nouns._boost import _BOOST

#calss header
class _BOOSTS(_BOOST, ):
	def __init__(self,): 
		_BOOST.__init__(self)
		self.name = "BOOSTS"
		self.specie = 'nouns'
		self.basic = "boost"
		self.jsondata = {}
