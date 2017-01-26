

from xai.brain.wordbase.nouns._quiet import _QUIET

#calss header
class _QUIETER(_QUIET, ):
	def __init__(self,): 
		_QUIET.__init__(self)
		self.name = "QUIETER"
		self.specie = 'nouns'
		self.basic = "quiet"
		self.jsondata = {}
