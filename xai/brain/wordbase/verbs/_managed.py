

from xai.brain.wordbase.verbs._manage import _MANAGE

#calss header
class _MANAGED(_MANAGE, ):
	def __init__(self,): 
		_MANAGE.__init__(self)
		self.name = "MANAGED"
		self.specie = 'verbs'
		self.basic = "manage"
		self.jsondata = {}
