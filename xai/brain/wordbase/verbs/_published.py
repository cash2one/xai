

from xai.brain.wordbase.verbs._publish import _PUBLISH

#calss header
class _PUBLISHED(_PUBLISH, ):
	def __init__(self,): 
		_PUBLISH.__init__(self)
		self.name = "PUBLISHED"
		self.specie = 'verbs'
		self.basic = "publish"
		self.jsondata = {}
