

from xai.brain.wordbase.nouns._downgrade import _DOWNGRADE

#calss header
class _DOWNGRADED(_DOWNGRADE, ):
	def __init__(self,): 
		_DOWNGRADE.__init__(self)
		self.name = "DOWNGRADED"
		self.specie = 'nouns'
		self.basic = "downgrade"
		self.jsondata = {}
