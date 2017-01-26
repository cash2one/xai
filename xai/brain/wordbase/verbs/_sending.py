

from xai.brain.wordbase.verbs._send import _SEND

#calss header
class _SENDING(_SEND, ):
	def __init__(self,): 
		_SEND.__init__(self)
		self.name = "SENDING"
		self.specie = 'verbs'
		self.basic = "send"
		self.jsondata = {}
