

from xai.brain.wordbase.verbs._analyse import _ANALYSE

#calss header
class _ANALYSED(_ANALYSE, ):
	def __init__(self,): 
		_ANALYSE.__init__(self)
		self.name = "ANALYSED"
		self.specie = 'verbs'
		self.basic = "analyse"
		self.jsondata = {}
