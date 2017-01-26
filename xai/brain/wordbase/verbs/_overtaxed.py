

from xai.brain.wordbase.verbs._overtax import _OVERTAX

#calss header
class _OVERTAXED(_OVERTAX, ):
	def __init__(self,): 
		_OVERTAX.__init__(self)
		self.name = "OVERTAXED"
		self.specie = 'verbs'
		self.basic = "overtax"
		self.jsondata = {}
