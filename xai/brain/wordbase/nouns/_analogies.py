

from xai.brain.wordbase.nouns._analogy import _ANALOGY

#calss header
class _ANALOGIES(_ANALOGY, ):
	def __init__(self,): 
		_ANALOGY.__init__(self)
		self.name = "ANALOGIES"
		self.specie = 'nouns'
		self.basic = "analogy"
		self.jsondata = {}
