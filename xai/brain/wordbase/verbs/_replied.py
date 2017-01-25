

from xai.brain.wordbase.verbs._reply import _REPLY

#calss header
class _REPLIED(_REPLY, ):
	def __init__(self,): 
		_REPLY.__init__(self)
		self.name = "REPLIED"
		self.specie = 'verbs'
		self.basic = "reply"
		self.jsondata = {}
