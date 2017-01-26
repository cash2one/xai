

from xai.brain.wordbase.verbs._write import _WRITE

#calss header
class _WRITES(_WRITE, ):
	def __init__(self,): 
		_WRITE.__init__(self)
		self.name = "WRITES"
		self.specie = 'verbs'
		self.basic = "write"
		self.jsondata = {}
