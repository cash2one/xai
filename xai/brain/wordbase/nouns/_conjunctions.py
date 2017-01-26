

from xai.brain.wordbase.nouns._conjunction import _CONJUNCTION

#calss header
class _CONJUNCTIONS(_CONJUNCTION, ):
	def __init__(self,): 
		_CONJUNCTION.__init__(self)
		self.name = "CONJUNCTIONS"
		self.specie = 'nouns'
		self.basic = "conjunction"
		self.jsondata = {}
