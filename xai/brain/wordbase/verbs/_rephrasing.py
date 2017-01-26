

from xai.brain.wordbase.verbs._rephrase import _REPHRASE

#calss header
class _REPHRASING(_REPHRASE, ):
	def __init__(self,): 
		_REPHRASE.__init__(self)
		self.name = "REPHRASING"
		self.specie = 'verbs'
		self.basic = "rephrase"
		self.jsondata = {}
