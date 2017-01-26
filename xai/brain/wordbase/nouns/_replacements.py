

from xai.brain.wordbase.nouns._replacement import _REPLACEMENT

#calss header
class _REPLACEMENTS(_REPLACEMENT, ):
	def __init__(self,): 
		_REPLACEMENT.__init__(self)
		self.name = "REPLACEMENTS"
		self.specie = 'nouns'
		self.basic = "replacement"
		self.jsondata = {}
