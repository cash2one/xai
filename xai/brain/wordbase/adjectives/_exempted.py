

from xai.brain.wordbase.adjectives._exempt import _EXEMPT

#calss header
class _EXEMPTED(_EXEMPT, ):
	def __init__(self,): 
		_EXEMPT.__init__(self)
		self.name = "EXEMPTED"
		self.specie = 'adjectives'
		self.basic = "exempt"
		self.jsondata = {}
