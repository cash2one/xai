

from xai.brain.wordbase.nouns._perm import _PERM

#calss header
class _PERMED(_PERM, ):
	def __init__(self,): 
		_PERM.__init__(self)
		self.name = "PERMED"
		self.specie = 'nouns'
		self.basic = "perm"
		self.jsondata = {}
