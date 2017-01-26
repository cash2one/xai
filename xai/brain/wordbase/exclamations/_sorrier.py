

from xai.brain.wordbase.exclamations._sorry import _SORRY

#calss header
class _SORRIER(_SORRY, ):
	def __init__(self,): 
		_SORRY.__init__(self)
		self.name = "SORRIER"
		self.specie = 'exclamations'
		self.basic = "sorry"
		self.jsondata = {}
