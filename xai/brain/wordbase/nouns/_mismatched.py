

from xai.brain.wordbase.nouns._mismatch import _MISMATCH

#calss header
class _MISMATCHED(_MISMATCH, ):
	def __init__(self,): 
		_MISMATCH.__init__(self)
		self.name = "MISMATCHED"
		self.specie = 'nouns'
		self.basic = "mismatch"
		self.jsondata = {}
