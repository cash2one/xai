

from xai.brain.wordbase.nouns._quiet import _QUIET

#calss header
class _QUIETED(_QUIET, ):
	def __init__(self,): 
		_QUIET.__init__(self)
		self.name = "QUIETED"
		self.specie = 'nouns'
		self.basic = "quiet"
		self.jsondata = {}
