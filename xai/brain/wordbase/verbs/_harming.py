

from xai.brain.wordbase.verbs._harm import _HARM

#calss header
class _HARMING(_HARM, ):
	def __init__(self,): 
		_HARM.__init__(self)
		self.name = "HARMING"
		self.specie = 'verbs'
		self.basic = "harm"
		self.jsondata = {}
