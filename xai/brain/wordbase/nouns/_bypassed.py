

from xai.brain.wordbase.nouns._bypass import _BYPASS

#calss header
class _BYPASSED(_BYPASS, ):
	def __init__(self,): 
		_BYPASS.__init__(self)
		self.name = "BYPASSED"
		self.specie = 'nouns'
		self.basic = "bypass"
		self.jsondata = {}
