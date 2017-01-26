

from xai.brain.wordbase.verbs._reply import _REPLY

#calss header
class _REPLYING(_REPLY, ):
	def __init__(self,): 
		_REPLY.__init__(self)
		self.name = "REPLYING"
		self.specie = 'verbs'
		self.basic = "reply"
		self.jsondata = {}
