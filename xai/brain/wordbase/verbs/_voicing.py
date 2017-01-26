

from xai.brain.wordbase.verbs._voice import _VOICE

#calss header
class _VOICING(_VOICE, ):
	def __init__(self,): 
		_VOICE.__init__(self)
		self.name = "VOICING"
		self.specie = 'verbs'
		self.basic = "voice"
		self.jsondata = {}
