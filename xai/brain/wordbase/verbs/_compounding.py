

from xai.brain.wordbase.verbs._compound import _COMPOUND

#calss header
class _COMPOUNDING(_COMPOUND, ):
	def __init__(self,): 
		_COMPOUND.__init__(self)
		self.name = "COMPOUNDING"
		self.specie = 'verbs'
		self.basic = "compound"
		self.jsondata = {}
