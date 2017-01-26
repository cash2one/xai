

from xai.brain.wordbase.nouns._curator import _CURATOR

#calss header
class _CURATORS(_CURATOR, ):
	def __init__(self,): 
		_CURATOR.__init__(self)
		self.name = "CURATORS"
		self.specie = 'nouns'
		self.basic = "curator"
		self.jsondata = {}
