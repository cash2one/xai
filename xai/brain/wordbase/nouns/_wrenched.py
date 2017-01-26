

from xai.brain.wordbase.nouns._wrench import _WRENCH

#calss header
class _WRENCHED(_WRENCH, ):
	def __init__(self,): 
		_WRENCH.__init__(self)
		self.name = "WRENCHED"
		self.specie = 'nouns'
		self.basic = "wrench"
		self.jsondata = {}
