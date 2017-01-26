

from xai.brain.wordbase.verbs._proscribe import _PROSCRIBE

#calss header
class _PROSCRIBED(_PROSCRIBE, ):
	def __init__(self,): 
		_PROSCRIBE.__init__(self)
		self.name = "PROSCRIBED"
		self.specie = 'verbs'
		self.basic = "proscribe"
		self.jsondata = {}
