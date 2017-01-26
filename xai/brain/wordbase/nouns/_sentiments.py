

from xai.brain.wordbase.nouns._sentiment import _SENTIMENT

#calss header
class _SENTIMENTS(_SENTIMENT, ):
	def __init__(self,): 
		_SENTIMENT.__init__(self)
		self.name = "SENTIMENTS"
		self.specie = 'nouns'
		self.basic = "sentiment"
		self.jsondata = {}
