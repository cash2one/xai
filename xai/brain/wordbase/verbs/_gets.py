

from xai.brain.wordbase.verbs._get import _GET

#calss header
class _GETS(_GET, ):
	def __init__(self,): 
		_GET.__init__(self)
		self.name = "GETS"
		self.specie = 'verbs'
		self.basic = "get"
		self.jsondata = {}
