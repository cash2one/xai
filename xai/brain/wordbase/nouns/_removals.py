

from xai.brain.wordbase.nouns._removal import _REMOVAL

#calss header
class _REMOVALS(_REMOVAL, ):
	def __init__(self,): 
		_REMOVAL.__init__(self)
		self.name = "REMOVALS"
		self.specie = 'nouns'
		self.basic = "removal"
		self.jsondata = {}
