

from xai.brain.wordbase.verbs._exclude import _EXCLUDE

#calss header
class _EXCLUDED(_EXCLUDE, ):
	def __init__(self,): 
		_EXCLUDE.__init__(self)
		self.name = "EXCLUDED"
		self.specie = 'verbs'
		self.basic = "exclude"
		self.jsondata = {}
