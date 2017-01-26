

from xai.brain.wordbase.nouns._buffer import _BUFFER

#calss header
class _BUFFERED(_BUFFER, ):
	def __init__(self,): 
		_BUFFER.__init__(self)
		self.name = "BUFFERED"
		self.specie = 'nouns'
		self.basic = "buffer"
		self.jsondata = {}
