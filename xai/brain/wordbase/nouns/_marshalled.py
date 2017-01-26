

from xai.brain.wordbase.nouns._marshal import _MARSHAL

#calss header
class _MARSHALLED(_MARSHAL, ):
	def __init__(self,): 
		_MARSHAL.__init__(self)
		self.name = "MARSHALLED"
		self.specie = 'nouns'
		self.basic = "marshal"
		self.jsondata = {}
