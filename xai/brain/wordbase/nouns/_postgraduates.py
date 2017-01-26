

from xai.brain.wordbase.nouns._postgraduate import _POSTGRADUATE

#calss header
class _POSTGRADUATES(_POSTGRADUATE, ):
	def __init__(self,): 
		_POSTGRADUATE.__init__(self)
		self.name = "POSTGRADUATES"
		self.specie = 'nouns'
		self.basic = "postgraduate"
		self.jsondata = {}
