

from xai.brain.wordbase.nouns._padlock import _PADLOCK

#calss header
class _PADLOCKED(_PADLOCK, ):
	def __init__(self,): 
		_PADLOCK.__init__(self)
		self.name = "PADLOCKED"
		self.specie = 'nouns'
		self.basic = "padlock"
		self.jsondata = {}
