

from xai.brain.wordbase.verbs._postdate import _POSTDATE

#calss header
class _POSTDATING(_POSTDATE, ):
	def __init__(self,): 
		_POSTDATE.__init__(self)
		self.name = "POSTDATING"
		self.specie = 'verbs'
		self.basic = "postdate"
		self.jsondata = {}
