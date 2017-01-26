

from xai.brain.wordbase.nouns._strip import _STRIP

#calss header
class _STRIPPED(_STRIP, ):
	def __init__(self,): 
		_STRIP.__init__(self)
		self.name = "STRIPPED"
		self.specie = 'nouns'
		self.basic = "strip"
		self.jsondata = {}
