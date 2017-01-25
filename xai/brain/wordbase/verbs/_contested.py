

from xai.brain.wordbase.verbs._contest import _CONTEST

#calss header
class _CONTESTED(_CONTEST, ):
	def __init__(self,): 
		_CONTEST.__init__(self)
		self.name = "CONTESTED"
		self.specie = 'verbs'
		self.basic = "contest"
		self.jsondata = {}
