

from xai.brain.wordbase.verbs._acquire import _ACQUIRE

#calss header
class _ACQUIRES(_ACQUIRE, ):
	def __init__(self,): 
		_ACQUIRE.__init__(self)
		self.name = "ACQUIRES"
		self.specie = 'verbs'
		self.basic = "acquire"
		self.jsondata = {}
