

from xai.brain.wordbase.verbs._invite import _INVITE

#calss header
class _INVITES(_INVITE, ):
	def __init__(self,): 
		_INVITE.__init__(self)
		self.name = "INVITES"
		self.specie = 'verbs'
		self.basic = "invite"
		self.jsondata = {}
