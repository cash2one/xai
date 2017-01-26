

from xai.brain.wordbase.verbs._ingest import _INGEST

#calss header
class _INGESTED(_INGEST, ):
	def __init__(self,): 
		_INGEST.__init__(self)
		self.name = "INGESTED"
		self.specie = 'verbs'
		self.basic = "ingest"
		self.jsondata = {}
