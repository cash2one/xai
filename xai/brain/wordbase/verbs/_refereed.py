

from xai.brain.wordbase.verbs._referee import _REFEREE

#calss header
class _REFEREED(_REFEREE, ):
	def __init__(self,): 
		_REFEREE.__init__(self)
		self.name = "REFEREED"
		self.specie = 'verbs'
		self.basic = "referee"
		self.jsondata = {}
