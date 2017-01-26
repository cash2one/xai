

from xai.brain.wordbase.nouns._broadcast import _BROADCAST

#calss header
class _BROADCASTED(_BROADCAST, ):
	def __init__(self,): 
		_BROADCAST.__init__(self)
		self.name = "BROADCASTED"
		self.specie = 'nouns'
		self.basic = "broadcast"
		self.jsondata = {}
