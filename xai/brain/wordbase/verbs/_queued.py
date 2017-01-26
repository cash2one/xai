

from xai.brain.wordbase.verbs._queue import _QUEUE

#calss header
class _QUEUED(_QUEUE, ):
	def __init__(self,): 
		_QUEUE.__init__(self)
		self.name = "QUEUED"
		self.specie = 'verbs'
		self.basic = "queue"
		self.jsondata = {}
