

from xai.brain.wordbase.verbs._rephrase import _REPHRASE

#calss header
class _REPHRASED(_REPHRASE, ):
	def __init__(self,): 
		_REPHRASE.__init__(self)
		self.name = "REPHRASED"
		self.specie = 'verbs'
		self.basic = "rephrase"
		self.jsondata = {}
