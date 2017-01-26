

from xai.brain.wordbase.nouns._referee import _REFEREE

#calss header
class _REFEREED(_REFEREE, ):
	def __init__(self,): 
		_REFEREE.__init__(self)
		self.name = "REFEREED"
		self.specie = 'nouns'
		self.basic = "referee"
		self.jsondata = {}
