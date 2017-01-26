

from xai.brain.wordbase.pronouns._mine import _MINE

#calss header
class _MINED(_MINE, ):
	def __init__(self,): 
		_MINE.__init__(self)
		self.name = "MINED"
		self.specie = 'pronouns'
		self.basic = "mine"
		self.jsondata = {}
