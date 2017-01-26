

from xai.brain.wordbase.adjectives._mild import _MILD

#calss header
class _MILDEST(_MILD, ):
	def __init__(self,): 
		_MILD.__init__(self)
		self.name = "MILDEST"
		self.specie = 'adjectives'
		self.basic = "mild"
		self.jsondata = {}
