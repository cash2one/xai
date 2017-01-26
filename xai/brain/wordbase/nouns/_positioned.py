

from xai.brain.wordbase.nouns._position import _POSITION

#calss header
class _POSITIONED(_POSITION, ):
	def __init__(self,): 
		_POSITION.__init__(self)
		self.name = "POSITIONED"
		self.specie = 'nouns'
		self.basic = "position"
		self.jsondata = {}
