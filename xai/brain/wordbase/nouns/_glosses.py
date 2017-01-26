

from xai.brain.wordbase.nouns._gloss import _GLOSS

#calss header
class _GLOSSES(_GLOSS, ):
	def __init__(self,): 
		_GLOSS.__init__(self)
		self.name = "GLOSSES"
		self.specie = 'nouns'
		self.basic = "gloss"
		self.jsondata = {}
