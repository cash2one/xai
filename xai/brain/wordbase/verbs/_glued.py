

from xai.brain.wordbase.verbs._glue import _GLUE

#calss header
class _GLUED(_GLUE, ):
	def __init__(self,): 
		_GLUE.__init__(self)
		self.name = "GLUED"
		self.specie = 'verbs'
		self.basic = "glue"
		self.jsondata = {}
