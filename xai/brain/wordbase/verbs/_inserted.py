

from xai.brain.wordbase.verbs._insert import _INSERT

#calss header
class _INSERTED(_INSERT, ):
	def __init__(self,): 
		_INSERT.__init__(self)
		self.name = "INSERTED"
		self.specie = 'verbs'
		self.basic = "insert"
		self.jsondata = {}
