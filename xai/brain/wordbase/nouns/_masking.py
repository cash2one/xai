

from xai.brain.wordbase.nouns._mask import _MASK

#calss header
class _MASKING(_MASK, ):
	def __init__(self,): 
		_MASK.__init__(self)
		self.name = "MASKING"
		self.specie = 'nouns'
		self.basic = "mask"
		self.jsondata = {}
