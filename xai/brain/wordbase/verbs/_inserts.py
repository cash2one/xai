

from xai.brain.wordbase.verbs._insert import _INSERT

#calss header
class _INSERTS(_INSERT, ):
	def __init__(self,): 
		_INSERT.__init__(self)
		self.name = "INSERTS"
		self.specie = 'verbs'
		self.basic = "insert"
		self.jsondata = {}
