

from xai.brain.wordbase.verbs._understand import _UNDERSTAND

#calss header
class _UNDERSTOOD(_UNDERSTAND, ):
	def __init__(self,): 
		_UNDERSTAND.__init__(self)
		self.name = "UNDERSTOOD"
		self.specie = 'verbs'
		self.basic = "understand"
		self.jsondata = {}
