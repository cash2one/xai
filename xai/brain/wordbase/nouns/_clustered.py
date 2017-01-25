

from xai.brain.wordbase.nouns._cluster import _CLUSTER

#calss header
class _CLUSTERED(_CLUSTER, ):
	def __init__(self,): 
		_CLUSTER.__init__(self)
		self.name = "CLUSTERED"
		self.specie = 'nouns'
		self.basic = "cluster"
		self.jsondata = {}
