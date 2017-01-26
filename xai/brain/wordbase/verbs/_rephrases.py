

from xai.brain.wordbase.verbs._rephrase import _REPHRASE

#calss header
class _REPHRASES(_REPHRASE, ):
	def __init__(self,): 
		_REPHRASE.__init__(self)
		self.name = "REPHRASES"
		self.specie = 'verbs'
		self.basic = "rephrase"
		self.jsondata = {}
