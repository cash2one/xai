

from xai.brain.wordbase.verbs._mistrust import _MISTRUST

#calss header
class _MISTRUSTED(_MISTRUST, ):
	def __init__(self,): 
		_MISTRUST.__init__(self)
		self.name = "MISTRUSTED"
		self.specie = 'verbs'
		self.basic = "mistrust"
		self.jsondata = {}
