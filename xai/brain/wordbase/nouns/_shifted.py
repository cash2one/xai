

from xai.brain.wordbase.nouns._shift import _SHIFT

#calss header
class _SHIFTED(_SHIFT, ):
	def __init__(self,): 
		_SHIFT.__init__(self)
		self.name = "SHIFTED"
		self.specie = 'nouns'
		self.basic = "shift"
		self.jsondata = {}
