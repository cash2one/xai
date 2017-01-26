

from xai.brain.wordbase.nouns._brown import _BROWN

#calss header
class _BROWNER(_BROWN, ):
	def __init__(self,): 
		_BROWN.__init__(self)
		self.name = "BROWNER"
		self.specie = 'nouns'
		self.basic = "brown"
		self.jsondata = {}
