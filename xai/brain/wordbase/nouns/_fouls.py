

from xai.brain.wordbase.nouns._foul import _FOUL

#calss header
class _FOULS(_FOUL, ):
	def __init__(self,): 
		_FOUL.__init__(self)
		self.name = "FOULS"
		self.specie = 'nouns'
		self.basic = "foul"
		self.jsondata = {}
