

from xai.brain.wordbase.nouns._commercial import _COMMERCIAL

#calss header
class _COMMERCIALS(_COMMERCIAL, ):
	def __init__(self,): 
		_COMMERCIAL.__init__(self)
		self.name = "COMMERCIALS"
		self.specie = 'nouns'
		self.basic = "commercial"
		self.jsondata = {}
