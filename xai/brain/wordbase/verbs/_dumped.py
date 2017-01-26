

from xai.brain.wordbase.verbs._dump import _DUMP

#calss header
class _DUMPED(_DUMP, ):
	def __init__(self,): 
		_DUMP.__init__(self)
		self.name = "DUMPED"
		self.specie = 'verbs'
		self.basic = "dump"
		self.jsondata = {}
