

from xai.brain.wordbase.nouns._rouge import _ROUGE

#calss header
class _ROUGED(_ROUGE, ):
	def __init__(self,): 
		_ROUGE.__init__(self)
		self.name = "ROUGED"
		self.specie = 'nouns'
		self.basic = "rouge"
		self.jsondata = {}
