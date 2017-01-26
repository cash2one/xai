

from xai.brain.wordbase.verbs._voice import _VOICE

#calss header
class _VOICES(_VOICE, ):
	def __init__(self,): 
		_VOICE.__init__(self)
		self.name = "VOICES"
		self.specie = 'verbs'
		self.basic = "voice"
		self.jsondata = {}
