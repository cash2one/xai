

from xai.brain.wordbase.adjectives._grey import _GREY

#calss header
class _GREYER(_GREY, ):
	def __init__(self,): 
		_GREY.__init__(self)
		self.name = "GREYER"
		self.specie = 'adjectives'
		self.basic = "grey"
		self.jsondata = {}
