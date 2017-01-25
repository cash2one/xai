

from xai.brain.wordbase.verbs._mistreat import _MISTREAT

#calss header
class _MISTREATED(_MISTREAT, ):
	def __init__(self,): 
		_MISTREAT.__init__(self)
		self.name = "MISTREATED"
		self.specie = 'verbs'
		self.basic = "mistreat"
		self.jsondata = {}
