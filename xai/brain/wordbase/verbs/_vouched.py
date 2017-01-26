

from xai.brain.wordbase.verbs._vouch import _VOUCH

#calss header
class _VOUCHED(_VOUCH, ):
	def __init__(self,): 
		_VOUCH.__init__(self)
		self.name = "VOUCHED"
		self.specie = 'verbs'
		self.basic = "vouch"
		self.jsondata = {}
