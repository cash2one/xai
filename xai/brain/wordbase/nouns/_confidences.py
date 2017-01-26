

from xai.brain.wordbase.nouns._confidence import _CONFIDENCE

#calss header
class _CONFIDENCES(_CONFIDENCE, ):
	def __init__(self,): 
		_CONFIDENCE.__init__(self)
		self.name = "CONFIDENCES"
		self.specie = 'nouns'
		self.basic = "confidence"
		self.jsondata = {}
