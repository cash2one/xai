

from xai.brain.wordbase.nouns._alumna import _ALUMNA

#calss header
class _ALUMNAE(_ALUMNA, ):
	def __init__(self,): 
		_ALUMNA.__init__(self)
		self.name = "ALUMNAE"
		self.specie = 'nouns'
		self.basic = "alumna"
		self.jsondata = {}
