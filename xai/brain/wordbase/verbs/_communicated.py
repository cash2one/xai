

from xai.brain.wordbase.verbs._communicate import _COMMUNICATE

#calss header
class _COMMUNICATED(_COMMUNICATE, ):
	def __init__(self,): 
		_COMMUNICATE.__init__(self)
		self.name = "COMMUNICATED"
		self.specie = 'verbs'
		self.basic = "communicate"
		self.jsondata = {}
