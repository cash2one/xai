

from xai.brain.wordbase.verbs._buffer import _BUFFER

#calss header
class _BUFFERED(_BUFFER, ):
	def __init__(self,): 
		_BUFFER.__init__(self)
		self.name = "BUFFERED"
		self.specie = 'verbs'
		self.basic = "buffer"
		self.jsondata = {}
