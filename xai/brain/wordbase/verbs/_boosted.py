

from xai.brain.wordbase.verbs._boost import _BOOST

#calss header
class _BOOSTED(_BOOST, ):
	def __init__(self,): 
		_BOOST.__init__(self)
		self.name = "BOOSTED"
		self.specie = 'verbs'
		self.basic = "boost"
		self.jsondata = {}
