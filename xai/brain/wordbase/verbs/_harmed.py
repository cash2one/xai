

from xai.brain.wordbase.verbs._harm import _HARM

#calss header
class _HARMED(_HARM, ):
	def __init__(self,): 
		_HARM.__init__(self)
		self.name = "HARMED"
		self.specie = 'verbs'
		self.basic = "harm"
		self.jsondata = {}
