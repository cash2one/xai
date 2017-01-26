

from xai.brain.wordbase.nouns._mute import _MUTE

#calss header
class _MUTING(_MUTE, ):
	def __init__(self,): 
		_MUTE.__init__(self)
		self.name = "MUTING"
		self.specie = 'nouns'
		self.basic = "mute"
		self.jsondata = {}
