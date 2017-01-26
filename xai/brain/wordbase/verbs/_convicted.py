

from xai.brain.wordbase.verbs._convict import _CONVICT

#calss header
class _CONVICTED(_CONVICT, ):
	def __init__(self,): 
		_CONVICT.__init__(self)
		self.name = "CONVICTED"
		self.specie = 'verbs'
		self.basic = "convict"
		self.jsondata = {}
