

from xai.brain.wordbase.nouns._hebrew import _HEBREW

#calss header
class _HEBREWS(_HEBREW, ):
	def __init__(self,): 
		_HEBREW.__init__(self)
		self.name = "HEBREWS"
		self.specie = 'nouns'
		self.basic = "hebrew"
		self.jsondata = {}
