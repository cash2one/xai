

from xai.brain.wordbase.verbs._administer import _ADMINISTER

#calss header
class _ADMINISTERS(_ADMINISTER, ):
	def __init__(self,): 
		_ADMINISTER.__init__(self)
		self.name = "ADMINISTERS"
		self.specie = 'verbs'
		self.basic = "administer"
		self.jsondata = {}
