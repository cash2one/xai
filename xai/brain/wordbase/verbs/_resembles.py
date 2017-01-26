

from xai.brain.wordbase.verbs._resemble import _RESEMBLE

#calss header
class _RESEMBLES(_RESEMBLE, ):
	def __init__(self,): 
		_RESEMBLE.__init__(self)
		self.name = "RESEMBLES"
		self.specie = 'verbs'
		self.basic = "resemble"
		self.jsondata = {}
