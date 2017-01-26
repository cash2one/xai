

from xai.brain.wordbase.nouns._batch import _BATCH

#calss header
class _BATCHED(_BATCH, ):
	def __init__(self,): 
		_BATCH.__init__(self)
		self.name = "BATCHED"
		self.specie = 'nouns'
		self.basic = "batch"
		self.jsondata = {}
