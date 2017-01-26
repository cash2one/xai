

from xai.brain.wordbase.nouns._collation import _COLLATION

#calss header
class _COLLATIONS(_COLLATION, ):
	def __init__(self,): 
		_COLLATION.__init__(self)
		self.name = "COLLATIONS"
		self.specie = 'nouns'
		self.basic = "collation"
		self.jsondata = {}
