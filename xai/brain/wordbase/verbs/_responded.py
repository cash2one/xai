

from xai.brain.wordbase.verbs._respond import _RESPOND

#calss header
class _RESPONDED(_RESPOND, ):
	def __init__(self,): 
		_RESPOND.__init__(self)
		self.name = "RESPONDED"
		self.specie = 'verbs'
		self.basic = "respond"
		self.jsondata = {}
