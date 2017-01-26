

from xai.brain.wordbase.nouns._trademark import _TRADEMARK

#calss header
class _TRADEMARKED(_TRADEMARK, ):
	def __init__(self,): 
		_TRADEMARK.__init__(self)
		self.name = "TRADEMARKED"
		self.specie = 'nouns'
		self.basic = "trademark"
		self.jsondata = {}
