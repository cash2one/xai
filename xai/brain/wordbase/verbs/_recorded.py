

from xai.brain.wordbase.verbs._record import _RECORD

#calss header
class _RECORDED(_RECORD, ):
	def __init__(self,): 
		_RECORD.__init__(self)
		self.name = "RECORDED"
		self.specie = 'verbs'
		self.basic = "record"
		self.jsondata = {}
