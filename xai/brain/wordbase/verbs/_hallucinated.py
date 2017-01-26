

from xai.brain.wordbase.verbs._hallucinate import _HALLUCINATE

#calss header
class _HALLUCINATED(_HALLUCINATE, ):
	def __init__(self,): 
		_HALLUCINATE.__init__(self)
		self.name = "HALLUCINATED"
		self.specie = 'verbs'
		self.basic = "hallucinate"
		self.jsondata = {}
