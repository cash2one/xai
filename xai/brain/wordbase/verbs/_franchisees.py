

from xai.brain.wordbase.verbs._franchise import _FRANCHISE

#calss header
class _FRANCHISEES(_FRANCHISE, ):
	def __init__(self,): 
		_FRANCHISE.__init__(self)
		self.name = "FRANCHISEES"
		self.specie = 'verbs'
		self.basic = "franchise"
		self.jsondata = {}
