

from xai.brain.wordbase.nouns._presupposition import _PRESUPPOSITION

#calss header
class _PRESUPPOSITIONS(_PRESUPPOSITION, ):
	def __init__(self,): 
		_PRESUPPOSITION.__init__(self)
		self.name = "PRESUPPOSITIONS"
		self.specie = 'nouns'
		self.basic = "presupposition"
		self.jsondata = {}
