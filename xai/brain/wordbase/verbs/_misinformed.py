

from xai.brain.wordbase.verbs._misinform import _MISINFORM

#calss header
class _MISINFORMED(_MISINFORM, ):
	def __init__(self,): 
		_MISINFORM.__init__(self)
		self.name = "MISINFORMED"
		self.specie = 'verbs'
		self.basic = "misinform"
		self.jsondata = {}
