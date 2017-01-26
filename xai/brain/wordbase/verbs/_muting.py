

from xai.brain.wordbase.verbs._mute import _MUTE

#calss header
class _MUTING(_MUTE, ):
	def __init__(self,): 
		_MUTE.__init__(self)
		self.name = "MUTING"
		self.specie = 'verbs'
		self.basic = "mute"
		self.jsondata = {}
