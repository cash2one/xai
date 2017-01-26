

from xai.brain.wordbase.adjectives._classified import _CLASSIFIED

#calss header
class _CLASSIFIEDS(_CLASSIFIED, ):
	def __init__(self,): 
		_CLASSIFIED.__init__(self)
		self.name = "CLASSIFIEDS"
		self.specie = 'adjectives'
		self.basic = "classified"
		self.jsondata = {}
