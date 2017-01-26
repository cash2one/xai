

from xai.brain.wordbase.verbs._officiate import _OFFICIATE

#calss header
class _OFFICIATING(_OFFICIATE, ):
	def __init__(self,): 
		_OFFICIATE.__init__(self)
		self.name = "OFFICIATING"
		self.specie = 'verbs'
		self.basic = "officiate"
		self.jsondata = {}
