

from xai.brain.wordbase.nouns._similarity import _SIMILARITY

#calss header
class _SIMILARITIES(_SIMILARITY, ):
	def __init__(self,): 
		_SIMILARITY.__init__(self)
		self.name = "SIMILARITIES"
		self.specie = 'nouns'
		self.basic = "similarity"
		self.jsondata = {}
