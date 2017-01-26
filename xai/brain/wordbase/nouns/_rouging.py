

from xai.brain.wordbase.nouns._rouge import _ROUGE

#calss header
class _ROUGING(_ROUGE, ):
	def __init__(self,): 
		_ROUGE.__init__(self)
		self.name = "ROUGING"
		self.specie = 'nouns'
		self.basic = "rouge"
		self.jsondata = {}
