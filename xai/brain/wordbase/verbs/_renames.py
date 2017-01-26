

from xai.brain.wordbase.verbs._rename import _RENAME

#calss header
class _RENAMES(_RENAME, ):
	def __init__(self,): 
		_RENAME.__init__(self)
		self.name = "RENAMES"
		self.specie = 'verbs'
		self.basic = "rename"
		self.jsondata = {}
