

from xai.brain.wordbase.nouns._glue import _GLUE

#calss header
class _GLUEING(_GLUE, ):
	def __init__(self,): 
		_GLUE.__init__(self)
		self.name = "GLUEING"
		self.specie = 'nouns'
		self.basic = "glue"
		self.jsondata = {}
