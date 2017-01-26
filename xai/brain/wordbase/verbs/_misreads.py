

from xai.brain.wordbase.verbs._misread import _MISREAD

#calss header
class _MISREADS(_MISREAD, ):
	def __init__(self,): 
		_MISREAD.__init__(self)
		self.name = "MISREADS"
		self.specie = 'verbs'
		self.basic = "misread"
		self.jsondata = {}
