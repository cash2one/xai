

from xai.brain.wordbase.verbs._arrest import _ARREST

#calss header
class _ARRESTED(_ARREST, ):
	def __init__(self,): 
		_ARREST.__init__(self)
		self.name = "ARRESTED"
		self.specie = 'verbs'
		self.basic = "arrest"
		self.jsondata = {}
