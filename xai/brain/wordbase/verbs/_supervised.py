

from xai.brain.wordbase.verbs._supervise import _SUPERVISE

#calss header
class _SUPERVISED(_SUPERVISE, ):
	def __init__(self,): 
		_SUPERVISE.__init__(self)
		self.name = "SUPERVISED"
		self.specie = 'verbs'
		self.basic = "supervise"
		self.jsondata = {}
