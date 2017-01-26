

from xai.brain.wordbase.verbs._postdate import _POSTDATE

#calss header
class _POSTDATED(_POSTDATE, ):
	def __init__(self,): 
		_POSTDATE.__init__(self)
		self.name = "POSTDATED"
		self.specie = 'verbs'
		self.basic = "postdate"
		self.jsondata = {}
