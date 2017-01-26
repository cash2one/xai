

from xai.brain.wordbase.verbs._encrypt import _ENCRYPT

#calss header
class _ENCRYPTS(_ENCRYPT, ):
	def __init__(self,): 
		_ENCRYPT.__init__(self)
		self.name = "ENCRYPTS"
		self.specie = 'verbs'
		self.basic = "encrypt"
		self.jsondata = {}
