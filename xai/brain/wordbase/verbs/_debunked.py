

from xai.brain.wordbase.verbs._debunk import _DEBUNK

#calss header
class _DEBUNKED(_DEBUNK, ):
	def __init__(self,): 
		_DEBUNK.__init__(self)
		self.name = "DEBUNKED"
		self.specie = 'verbs'
		self.basic = "debunk"
		self.jsondata = {}
