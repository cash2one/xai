

from xai.brain.wordbase.nouns._phobia import _PHOBIA

#calss header
class _PHOBIAS(_PHOBIA, ):
	def __init__(self,): 
		_PHOBIA.__init__(self)
		self.name = "PHOBIAS"
		self.specie = 'nouns'
		self.basic = "phobia"
		self.jsondata = {}
