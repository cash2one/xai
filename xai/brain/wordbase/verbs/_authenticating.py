

from xai.brain.wordbase.verbs._authenticate import _AUTHENTICATE

#calss header
class _AUTHENTICATING(_AUTHENTICATE, ):
	def __init__(self,): 
		_AUTHENTICATE.__init__(self)
		self.name = "AUTHENTICATING"
		self.specie = 'verbs'
		self.basic = "authenticate"
		self.jsondata = {}
