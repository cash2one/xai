

from xai.brain.wordbase.verbs._brown import _BROWN

#calss header
class _BROWNER(_BROWN, ):
	def __init__(self,): 
		_BROWN.__init__(self)
		self.name = "BROWNER"
		self.specie = 'verbs'
		self.basic = "brown"
		self.jsondata = {}
