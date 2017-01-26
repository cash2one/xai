

from xai.brain.wordbase.verbs._filter import _FILTER

#calss header
class _FILTERS(_FILTER, ):
	def __init__(self,): 
		_FILTER.__init__(self)
		self.name = "FILTERS"
		self.specie = 'verbs'
		self.basic = "filter"
		self.jsondata = {}
