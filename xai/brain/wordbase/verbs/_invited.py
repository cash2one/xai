

from xai.brain.wordbase.verbs._invite import _INVITE

#calss header
class _INVITED(_INVITE, ):
	def __init__(self,): 
		_INVITE.__init__(self)
		self.name = "INVITED"
		self.specie = 'verbs'
		self.basic = "invite"
		self.jsondata = {}
