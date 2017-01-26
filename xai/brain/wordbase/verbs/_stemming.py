

from xai.brain.wordbase.verbs._stem import _STEM

#calss header
class _STEMMING(_STEM, ):
	def __init__(self,): 
		_STEM.__init__(self)
		self.name = "STEMMING"
		self.specie = 'verbs'
		self.basic = "stem"
		self.jsondata = {}
