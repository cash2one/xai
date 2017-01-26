

from xai.brain.wordbase.nouns._surgery import _SURGERY

#calss header
class _SURGERIES(_SURGERY, ):
	def __init__(self,): 
		_SURGERY.__init__(self)
		self.name = "SURGERIES"
		self.specie = 'nouns'
		self.basic = "surgery"
		self.jsondata = {}
