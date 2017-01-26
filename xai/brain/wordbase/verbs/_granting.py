

from xai.brain.wordbase.verbs._grant import _GRANT

#calss header
class _GRANTING(_GRANT, ):
	def __init__(self,): 
		_GRANT.__init__(self)
		self.name = "GRANTING"
		self.specie = 'verbs'
		self.basic = "grant"
		self.jsondata = {}
