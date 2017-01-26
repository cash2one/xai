

from xai.brain.wordbase.verbs._marshal import _MARSHAL

#calss header
class _MARSHALLED(_MARSHAL, ):
	def __init__(self,): 
		_MARSHAL.__init__(self)
		self.name = "MARSHALLED"
		self.specie = 'verbs'
		self.basic = "marshal"
		self.jsondata = {}
