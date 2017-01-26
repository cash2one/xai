

from xai.brain.wordbase.adjectives._independent import _INDEPENDENT

#calss header
class _INDEPENDENTS(_INDEPENDENT, ):
	def __init__(self,): 
		_INDEPENDENT.__init__(self)
		self.name = "INDEPENDENTS"
		self.specie = 'adjectives'
		self.basic = "independent"
		self.jsondata = {}
