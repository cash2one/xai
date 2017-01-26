

from xai.brain.wordbase.adverbs._pray import _PRAY

#calss header
class _PRAYING(_PRAY, ):
	def __init__(self,): 
		_PRAY.__init__(self)
		self.name = "PRAYING"
		self.specie = 'adverbs'
		self.basic = "pray"
		self.jsondata = {}
