

from xai.brain.wordbase.verbs._regulate import _REGULATE

#calss header
class _REGULATES(_REGULATE, ):
	def __init__(self,): 
		_REGULATE.__init__(self)
		self.name = "REGULATES"
		self.specie = 'verbs'
		self.basic = "regulate"
		self.jsondata = {}
