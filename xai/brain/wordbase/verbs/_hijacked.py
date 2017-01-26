

from xai.brain.wordbase.verbs._hijack import _HIJACK

#calss header
class _HIJACKED(_HIJACK, ):
	def __init__(self,): 
		_HIJACK.__init__(self)
		self.name = "HIJACKED"
		self.specie = 'verbs'
		self.basic = "hijack"
		self.jsondata = {}
