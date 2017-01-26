

from xai.brain.wordbase.nouns._voice import _VOICE

#calss header
class _VOICES(_VOICE, ):
	def __init__(self,): 
		_VOICE.__init__(self)
		self.name = "VOICES"
		self.specie = 'nouns'
		self.basic = "voice"
		self.jsondata = {}
