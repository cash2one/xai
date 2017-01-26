

from xai.brain.wordbase.verbs._administer import _ADMINISTER

#calss header
class _ADMINISTERED(_ADMINISTER, ):
	def __init__(self,): 
		_ADMINISTER.__init__(self)
		self.name = "ADMINISTERED"
		self.specie = 'verbs'
		self.basic = "administer"
		self.jsondata = {}
