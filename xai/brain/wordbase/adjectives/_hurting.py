

from xai.brain.wordbase.adjectives._hurt import _HURT

#calss header
class _HURTING(_HURT, ):
	def __init__(self,): 
		_HURT.__init__(self)
		self.name = "HURTING"
		self.specie = 'adjectives'
		self.basic = "hurt"
		self.jsondata = {}
