

from xai.brain.wordbase.verbs._disconnect import _DISCONNECT

#calss header
class _DISCONNECTING(_DISCONNECT, ):
	def __init__(self,): 
		_DISCONNECT.__init__(self)
		self.name = "DISCONNECTING"
		self.specie = 'verbs'
		self.basic = "disconnect"
		self.jsondata = {}
