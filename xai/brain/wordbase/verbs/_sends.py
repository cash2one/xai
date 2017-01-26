

from xai.brain.wordbase.verbs._send import _SEND

#calss header
class _SENDS(_SEND, ):
	def __init__(self,): 
		_SEND.__init__(self)
		self.name = "SENDS"
		self.specie = 'verbs'
		self.basic = "send"
		self.jsondata = {}
