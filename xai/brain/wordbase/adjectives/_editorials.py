

from xai.brain.wordbase.adjectives._editorial import _EDITORIAL

#calss header
class _EDITORIALS(_EDITORIAL, ):
	def __init__(self,): 
		_EDITORIAL.__init__(self)
		self.name = "EDITORIALS"
		self.specie = 'adjectives'
		self.basic = "editorial"
		self.jsondata = {}
