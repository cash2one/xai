

from xai.brain.wordbase.verbs._donate import _DONATE

#calss header
class _DONATING(_DONATE, ):
	def __init__(self,): 
		_DONATE.__init__(self)
		self.name = "DONATING"
		self.specie = 'verbs'
		self.basic = "donate"
		self.jsondata = {}
