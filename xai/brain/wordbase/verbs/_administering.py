

from xai.brain.wordbase.verbs._administer import _ADMINISTER

#calss header
class _ADMINISTERING(_ADMINISTER, ):
	def __init__(self,): 
		_ADMINISTER.__init__(self)
		self.name = "ADMINISTERING"
		self.specie = 'verbs'
		self.basic = "administer"
		self.jsondata = {}
