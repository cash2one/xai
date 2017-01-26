

from xai.brain.wordbase.verbs._redirect import _REDIRECT

#calss header
class _REDIRECTS(_REDIRECT, ):
	def __init__(self,): 
		_REDIRECT.__init__(self)
		self.name = "REDIRECTS"
		self.specie = 'verbs'
		self.basic = "redirect"
		self.jsondata = {}
