

from xai.brain.wordbase.verbs._deserve import _DESERVE

#calss header
class _DESERVES(_DESERVE, ):
	def __init__(self,): 
		_DESERVE.__init__(self)
		self.name = "DESERVES"
		self.specie = 'verbs'
		self.basic = "deserve"
		self.jsondata = {}
