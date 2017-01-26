

from xai.brain.wordbase.verbs._archive import _ARCHIVE

#calss header
class _ARCHIVED(_ARCHIVE, ):
	def __init__(self,): 
		_ARCHIVE.__init__(self)
		self.name = "ARCHIVED"
		self.specie = 'verbs'
		self.basic = "archive"
		self.jsondata = {}
