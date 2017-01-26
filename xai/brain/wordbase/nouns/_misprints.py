

from xai.brain.wordbase.nouns._misprint import _MISPRINT

#calss header
class _MISPRINTS(_MISPRINT, ):
	def __init__(self,): 
		_MISPRINT.__init__(self)
		self.name = "MISPRINTS"
		self.specie = 'nouns'
		self.basic = "misprint"
		self.jsondata = {}
