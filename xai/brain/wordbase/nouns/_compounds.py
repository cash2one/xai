

from xai.brain.wordbase.nouns._compound import _COMPOUND

#calss header
class _COMPOUNDS(_COMPOUND, ):
	def __init__(self,): 
		_COMPOUND.__init__(self)
		self.name = "COMPOUNDS"
		self.specie = 'nouns'
		self.basic = "compound"
		self.jsondata = {}
