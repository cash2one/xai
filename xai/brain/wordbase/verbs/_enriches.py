

from xai.brain.wordbase.verbs._enrich import _ENRICH

#calss header
class _ENRICHES(_ENRICH, ):
	def __init__(self,): 
		_ENRICH.__init__(self)
		self.name = "ENRICHES"
		self.specie = 'verbs'
		self.basic = "enrich"
		self.jsondata = {}
