

from xai.brain.wordbase.verbs._release import _RELEASE

#calss header
class _RELEASED(_RELEASE, ):
	def __init__(self,): 
		_RELEASE.__init__(self)
		self.name = "RELEASED"
		self.specie = 'verbs'
		self.basic = "release"
		self.jsondata = {}
