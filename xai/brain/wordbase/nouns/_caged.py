

from xai.brain.wordbase.nouns._cage import _CAGE

#calss header
class _CAGED(_CAGE, ):
	def __init__(self,): 
		_CAGE.__init__(self)
		self.name = "CAGED"
		self.specie = 'nouns'
		self.basic = "cage"
		self.jsondata = {}
