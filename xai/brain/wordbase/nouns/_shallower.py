

from xai.brain.wordbase.nouns._shallow import _SHALLOW

#calss header
class _SHALLOWER(_SHALLOW, ):
	def __init__(self,): 
		_SHALLOW.__init__(self)
		self.name = "SHALLOWER"
		self.specie = 'nouns'
		self.basic = "shallow"
		self.jsondata = {}
