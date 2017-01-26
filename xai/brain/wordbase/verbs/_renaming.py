

from xai.brain.wordbase.verbs._rename import _RENAME

#calss header
class _RENAMING(_RENAME, ):
	def __init__(self,): 
		_RENAME.__init__(self)
		self.name = "RENAMING"
		self.specie = 'verbs'
		self.basic = "rename"
		self.jsondata = {}
