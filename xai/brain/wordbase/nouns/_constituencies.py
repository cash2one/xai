

from xai.brain.wordbase.nouns._constituency import _CONSTITUENCY

#calss header
class _CONSTITUENCIES(_CONSTITUENCY, ):
	def __init__(self,): 
		_CONSTITUENCY.__init__(self)
		self.name = "CONSTITUENCIES"
		self.specie = 'nouns'
		self.basic = "constituency"
		self.jsondata = {}
