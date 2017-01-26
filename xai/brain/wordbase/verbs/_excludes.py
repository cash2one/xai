

from xai.brain.wordbase.verbs._exclude import _EXCLUDE

#calss header
class _EXCLUDES(_EXCLUDE, ):
	def __init__(self,): 
		_EXCLUDE.__init__(self)
		self.name = "EXCLUDES"
		self.specie = 'verbs'
		self.basic = "exclude"
		self.jsondata = {}
