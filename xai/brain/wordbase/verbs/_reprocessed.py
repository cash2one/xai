

from xai.brain.wordbase.verbs._reprocess import _REPROCESS

#calss header
class _REPROCESSED(_REPROCESS, ):
	def __init__(self,): 
		_REPROCESS.__init__(self)
		self.name = "REPROCESSED"
		self.specie = 'verbs'
		self.basic = "reprocess"
		self.jsondata = {}
