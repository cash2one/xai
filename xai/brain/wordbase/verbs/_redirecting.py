

from xai.brain.wordbase.verbs._redirect import _REDIRECT

#calss header
class _REDIRECTING(_REDIRECT, ):
	def __init__(self,): 
		_REDIRECT.__init__(self)
		self.name = "REDIRECTING"
		self.specie = 'verbs'
		self.basic = "redirect"
		self.jsondata = {}
