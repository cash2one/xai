

from xai.brain.wordbase.adjectives._master import _MASTER

#calss header
class _MASTERED(_MASTER, ):
	def __init__(self,): 
		_MASTER.__init__(self)
		self.name = "MASTERED"
		self.specie = 'adjectives'
		self.basic = "master"
		self.jsondata = {}
