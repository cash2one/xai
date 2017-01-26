

from xai.brain.wordbase.verbs._assassinate import _ASSASSINATE

#calss header
class _ASSASSINATED(_ASSASSINATE, ):
	def __init__(self,): 
		_ASSASSINATE.__init__(self)
		self.name = "ASSASSINATED"
		self.specie = 'verbs'
		self.basic = "assassinate"
		self.jsondata = {}
