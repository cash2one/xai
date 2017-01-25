

from xai.brain.wordbase.nouns._rouge import _ROUGE

#calss header
class _ROUGES(_ROUGE, ):
	def __init__(self,): 
		self.name = "ROUGES"
		self.basic = "rouge"
		self.jsondata = {}
