

from xai.brain.wordbase.verbs._notify import _NOTIFY

#calss header
class _NOTIFIED(_NOTIFY, ):
	def __init__(self,): 
		_NOTIFY.__init__(self)
		self.name = "NOTIFIED"
		self.specie = 'verbs'
		self.basic = "notify"
		self.jsondata = {}
