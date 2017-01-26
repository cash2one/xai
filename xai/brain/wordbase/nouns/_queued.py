

from xai.brain.wordbase.nouns._queue import _QUEUE

#calss header
class _QUEUED(_QUEUE, ):
	def __init__(self,): 
		_QUEUE.__init__(self)
		self.name = "QUEUED"
		self.specie = 'nouns'
		self.basic = "queue"
		self.jsondata = {}
