

from xai.brain.wordbase.verbs._mock import _MOCK

#calss header
class _MOCKED(_MOCK, ):
	def __init__(self,): 
		_MOCK.__init__(self)
		self.name = "MOCKED"
		self.specie = 'verbs'
		self.basic = "mock"
		self.jsondata = {}
