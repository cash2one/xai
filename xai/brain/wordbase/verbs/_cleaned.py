

from xai.brain.wordbase.verbs._clean import _CLEAN

#calss header
class _CLEANED(_CLEAN, ):
	def __init__(self,): 
		_CLEAN.__init__(self)
		self.name = "CLEANED"
		self.specie = 'verbs'
		self.basic = "clean"
		self.jsondata = {}
