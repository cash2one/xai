

from xai.brain.wordbase.verbs._query import _QUERY

#calss header
class _QUERIED(_QUERY, ):
	def __init__(self,): 
		_QUERY.__init__(self)
		self.name = "QUERIED"
		self.specie = 'verbs'
		self.basic = "query"
		self.jsondata = {}
