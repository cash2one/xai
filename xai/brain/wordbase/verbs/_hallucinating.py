

from xai.brain.wordbase.verbs._hallucinate import _HALLUCINATE

#calss header
class _HALLUCINATING(_HALLUCINATE, ):
	def __init__(self,): 
		_HALLUCINATE.__init__(self)
		self.name = "HALLUCINATING"
		self.specie = 'verbs'
		self.basic = "hallucinate"
		self.jsondata = {}
