

from xai.brain.wordbase.verbs._enrich import _ENRICH

#calss header
class _ENRICHED(_ENRICH, ):
	def __init__(self,): 
		_ENRICH.__init__(self)
		self.name = "ENRICHED"
		self.specie = 'verbs'
		self.basic = "enrich"
		self.jsondata = {}
