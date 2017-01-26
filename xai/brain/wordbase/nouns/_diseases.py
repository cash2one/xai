

from xai.brain.wordbase.nouns._disease import _DISEASE

#calss header
class _DISEASES(_DISEASE, ):
	def __init__(self,): 
		_DISEASE.__init__(self)
		self.name = "DISEASES"
		self.specie = 'nouns'
		self.basic = "disease"
		self.jsondata = {}
