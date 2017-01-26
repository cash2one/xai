

from xai.brain.wordbase.nouns._hallucination import _HALLUCINATION

#calss header
class _HALLUCINATIONS(_HALLUCINATION, ):
	def __init__(self,): 
		_HALLUCINATION.__init__(self)
		self.name = "HALLUCINATIONS"
		self.specie = 'nouns'
		self.basic = "hallucination"
		self.jsondata = {}
