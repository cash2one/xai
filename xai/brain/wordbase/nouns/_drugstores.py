

from xai.brain.wordbase.nouns._drugstore import _DRUGSTORE

#calss header
class _DRUGSTORES(_DRUGSTORE, ):
	def __init__(self,): 
		_DRUGSTORE.__init__(self)
		self.name = "DRUGSTORES"
		self.specie = 'nouns'
		self.basic = "drugstore"
		self.jsondata = {}
