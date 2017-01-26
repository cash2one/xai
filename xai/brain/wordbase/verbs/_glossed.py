

from xai.brain.wordbase.verbs._gloss import _GLOSS

#calss header
class _GLOSSED(_GLOSS, ):
	def __init__(self,): 
		_GLOSS.__init__(self)
		self.name = "GLOSSED"
		self.specie = 'verbs'
		self.basic = "gloss"
		self.jsondata = {}
