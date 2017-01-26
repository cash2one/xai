

from xai.brain.wordbase.verbs._ticket import _TICKET

#calss header
class _TICKETED(_TICKET, ):
	def __init__(self,): 
		_TICKET.__init__(self)
		self.name = "TICKETED"
		self.specie = 'verbs'
		self.basic = "ticket"
		self.jsondata = {}
