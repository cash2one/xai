

from xai.brain.wordbase.verbs._contaminate import _CONTAMINATE

#calss header
class _CONTAMINATED(_CONTAMINATE, ):
	def __init__(self,): 
		_CONTAMINATE.__init__(self)
		self.name = "CONTAMINATED"
		self.specie = 'verbs'
		self.basic = "contaminate"
		self.jsondata = {}
