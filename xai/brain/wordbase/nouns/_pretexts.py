

from xai.brain.wordbase.nouns._pretext import _PRETEXT

#calss header
class _PRETEXTS(_PRETEXT, ):
	def __init__(self,): 
		_PRETEXT.__init__(self)
		self.name = "PRETEXTS"
		self.specie = 'nouns'
		self.basic = "pretext"
		self.jsondata = {}
