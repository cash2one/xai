

from xai.brain.wordbase.nouns._gloss import _GLOSS

#calss header
class _GLOSSED(_GLOSS, ):
	def __init__(self,): 
		_GLOSS.__init__(self)
		self.name = "GLOSSED"
		self.specie = 'nouns'
		self.basic = "gloss"
		self.jsondata = {}
