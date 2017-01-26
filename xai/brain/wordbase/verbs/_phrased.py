

from xai.brain.wordbase.verbs._phrase import _PHRASE

#calss header
class _PHRASED(_PHRASE, ):
	def __init__(self,): 
		_PHRASE.__init__(self)
		self.name = "PHRASED"
		self.specie = 'verbs'
		self.basic = "phrase"
		self.jsondata = {}
