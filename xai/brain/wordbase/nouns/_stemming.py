

from xai.brain.wordbase.nouns._stem import _STEM

#calss header
class _STEMMING(_STEM, ):
	def __init__(self,): 
		_STEM.__init__(self)
		self.name = "STEMMING"
		self.specie = 'nouns'
		self.basic = "stem"
		self.jsondata = {}
