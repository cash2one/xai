

from xai.brain.wordbase.verbs._misjudge import _MISJUDGE

#calss header
class _MISJUDGED(_MISJUDGE, ):
	def __init__(self,): 
		_MISJUDGE.__init__(self)
		self.name = "MISJUDGED"
		self.specie = 'verbs'
		self.basic = "misjudge"
		self.jsondata = {}
