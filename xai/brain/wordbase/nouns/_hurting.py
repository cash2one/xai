

from xai.brain.wordbase.nouns._hurt import _HURT

#calss header
class _HURTING(_HURT, ):
	def __init__(self,): 
		_HURT.__init__(self)
		self.name = "HURTING"
		self.specie = 'nouns'
		self.basic = "hurt"
		self.jsondata = {}
