

from xai.brain.wordbase.verbs._exist import _EXIST

#calss header
class _EXISTS(_EXIST, ):
	def __init__(self,): 
		_EXIST.__init__(self)
		self.name = "EXISTS"
		self.specie = 'verbs'
		self.basic = "exist"
		self.jsondata = {}
