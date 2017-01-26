

from xai.brain.wordbase.nouns._boost import _BOOST

#calss header
class _BOOSTED(_BOOST, ):
	def __init__(self,): 
		_BOOST.__init__(self)
		self.name = "BOOSTED"
		self.specie = 'nouns'
		self.basic = "boost"
		self.jsondata = {}
