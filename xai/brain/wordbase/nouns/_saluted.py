

from xai.brain.wordbase.nouns._salute import _SALUTE

#calss header
class _SALUTED(_SALUTE, ):
	def __init__(self,): 
		_SALUTE.__init__(self)
		self.name = "SALUTED"
		self.specie = 'nouns'
		self.basic = "salute"
		self.jsondata = {}
