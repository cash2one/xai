

from xai.brain.wordbase.nouns._songwriter import _SONGWRITER

#calss header
class _SONGWRITERS(_SONGWRITER, ):
	def __init__(self,): 
		_SONGWRITER.__init__(self)
		self.name = "SONGWRITERS"
		self.specie = 'nouns'
		self.basic = "songwriter"
		self.jsondata = {}
