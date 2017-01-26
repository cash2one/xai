

from xai.brain.wordbase.nouns._hyphen import _HYPHEN

#calss header
class _HYPHENS(_HYPHEN, ):
	def __init__(self,): 
		_HYPHEN.__init__(self)
		self.name = "HYPHENS"
		self.specie = 'nouns'
		self.basic = "hyphen"
		self.jsondata = {}
