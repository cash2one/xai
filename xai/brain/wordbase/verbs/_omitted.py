

from xai.brain.wordbase.verbs._omit import _OMIT

#calss header
class _OMITTED(_OMIT, ):
	def __init__(self,): 
		_OMIT.__init__(self)
		self.name = "OMITTED"
		self.specie = 'verbs'
		self.basic = "omit"
		self.jsondata = {}
