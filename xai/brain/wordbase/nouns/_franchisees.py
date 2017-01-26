

from xai.brain.wordbase.nouns._franchise import _FRANCHISE

#calss header
class _FRANCHISEES(_FRANCHISE, ):
	def __init__(self,): 
		_FRANCHISE.__init__(self)
		self.name = "FRANCHISEES"
		self.specie = 'nouns'
		self.basic = "franchise"
		self.jsondata = {}
