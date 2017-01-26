

from xai.brain.wordbase.verbs._pray import _PRAY

#calss header
class _PRAYING(_PRAY, ):
	def __init__(self,): 
		_PRAY.__init__(self)
		self.name = "PRAYING"
		self.specie = 'verbs'
		self.basic = "pray"
		self.jsondata = {}
