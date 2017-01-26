

from xai.brain.wordbase.nouns._payload import _PAYLOAD

#calss header
class _PAYLOADS(_PAYLOAD, ):
	def __init__(self,): 
		_PAYLOAD.__init__(self)
		self.name = "PAYLOADS"
		self.specie = 'nouns'
		self.basic = "payload"
		self.jsondata = {}
