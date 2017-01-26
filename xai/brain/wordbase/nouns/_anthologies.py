

from xai.brain.wordbase.nouns._anthology import _ANTHOLOGY

#calss header
class _ANTHOLOGIES(_ANTHOLOGY, ):
	def __init__(self,): 
		_ANTHOLOGY.__init__(self)
		self.name = "ANTHOLOGIES"
		self.specie = 'nouns'
		self.basic = "anthology"
		self.jsondata = {}
