

from xai.brain.wordbase.verbs._exempt import _EXEMPT

#calss header
class _EXEMPTED(_EXEMPT, ):
	def __init__(self,): 
		_EXEMPT.__init__(self)
		self.name = "EXEMPTED"
		self.specie = 'verbs'
		self.basic = "exempt"
		self.jsondata = {}
