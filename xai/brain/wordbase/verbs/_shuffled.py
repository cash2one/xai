

from xai.brain.wordbase.verbs._shuffle import _SHUFFLE

#calss header
class _SHUFFLED(_SHUFFLE, ):
	def __init__(self,): 
		_SHUFFLE.__init__(self)
		self.name = "SHUFFLED"
		self.specie = 'verbs'
		self.basic = "shuffle"
		self.jsondata = {}
