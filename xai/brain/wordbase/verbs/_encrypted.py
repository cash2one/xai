

from xai.brain.wordbase.verbs._encrypt import _ENCRYPT

#calss header
class _ENCRYPTED(_ENCRYPT, ):
	def __init__(self,): 
		_ENCRYPT.__init__(self)
		self.name = "ENCRYPTED"
		self.specie = 'verbs'
		self.basic = "encrypt"
		self.jsondata = {}
