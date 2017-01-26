

from xai.brain.wordbase.verbs._fetch import _FETCH

#calss header
class _FETCHED(_FETCH, ):
	def __init__(self,): 
		_FETCH.__init__(self)
		self.name = "FETCHED"
		self.specie = 'verbs'
		self.basic = "fetch"
		self.jsondata = {}
