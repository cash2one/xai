

from xai.brain.wordbase.verbs._participate import _PARTICIPATE

#calss header
class _PARTICIPATED(_PARTICIPATE, ):
	def __init__(self,): 
		_PARTICIPATE.__init__(self)
		self.name = "PARTICIPATED"
		self.specie = 'verbs'
		self.basic = "participate"
		self.jsondata = {}
