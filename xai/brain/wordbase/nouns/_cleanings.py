

from xai.brain.wordbase.nouns._cleaning import _CLEANING

#calss header
class _CLEANINGS(_CLEANING, ):
	def __init__(self,): 
		_CLEANING.__init__(self)
		self.name = "CLEANINGS"
		self.specie = 'nouns'
		self.basic = "cleaning"
		self.jsondata = {}
