

from xai.brain.wordbase.verbs._annotate import _ANNOTATE

#calss header
class _ANNOTATED(_ANNOTATE, ):
	def __init__(self,): 
		_ANNOTATE.__init__(self)
		self.name = "ANNOTATED"
		self.specie = 'verbs'
		self.basic = "annotate"
		self.jsondata = {}
