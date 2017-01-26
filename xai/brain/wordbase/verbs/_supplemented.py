

from xai.brain.wordbase.verbs._supplement import _SUPPLEMENT

#calss header
class _SUPPLEMENTED(_SUPPLEMENT, ):
	def __init__(self,): 
		_SUPPLEMENT.__init__(self)
		self.name = "SUPPLEMENTED"
		self.specie = 'verbs'
		self.basic = "supplement"
		self.jsondata = {}
