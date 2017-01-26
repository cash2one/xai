

from xai.brain.wordbase.nouns._grey import _GREY

#calss header
class _GREYED(_GREY, ):
	def __init__(self,): 
		_GREY.__init__(self)
		self.name = "GREYED"
		self.specie = 'nouns'
		self.basic = "grey"
		self.jsondata = {}
