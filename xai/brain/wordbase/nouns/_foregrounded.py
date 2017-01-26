

from xai.brain.wordbase.nouns._foreground import _FOREGROUND

#calss header
class _FOREGROUNDED(_FOREGROUND, ):
	def __init__(self,): 
		_FOREGROUND.__init__(self)
		self.name = "FOREGROUNDED"
		self.specie = 'nouns'
		self.basic = "foreground"
		self.jsondata = {}
