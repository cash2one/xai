

from xai.brain.wordbase.verbs._interrogate import _INTERROGATE

#calss header
class _INTERROGATED(_INTERROGATE, ):
	def __init__(self,): 
		_INTERROGATE.__init__(self)
		self.name = "INTERROGATED"
		self.specie = 'verbs'
		self.basic = "interrogate"
		self.jsondata = {}
