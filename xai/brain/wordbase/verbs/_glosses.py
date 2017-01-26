

from xai.brain.wordbase.verbs._gloss import _GLOSS

#calss header
class _GLOSSES(_GLOSS, ):
	def __init__(self,): 
		_GLOSS.__init__(self)
		self.name = "GLOSSES"
		self.specie = 'verbs'
		self.basic = "gloss"
		self.jsondata = {}
