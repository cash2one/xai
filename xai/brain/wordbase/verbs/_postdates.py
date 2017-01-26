

from xai.brain.wordbase.verbs._postdate import _POSTDATE

#calss header
class _POSTDATES(_POSTDATE, ):
	def __init__(self,): 
		_POSTDATE.__init__(self)
		self.name = "POSTDATES"
		self.specie = 'verbs'
		self.basic = "postdate"
		self.jsondata = {}
