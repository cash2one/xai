

from xai.brain.wordbase.verbs._referee import _REFEREE

#calss header
class _REFEREES(_REFEREE, ):
	def __init__(self,): 
		_REFEREE.__init__(self)
		self.name = "REFEREES"
		self.specie = 'verbs'
		self.basic = "referee"
		self.jsondata = {}
