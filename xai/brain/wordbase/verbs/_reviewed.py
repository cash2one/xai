

from xai.brain.wordbase.verbs._review import _REVIEW

#calss header
class _REVIEWED(_REVIEW, ):
	def __init__(self,): 
		_REVIEW.__init__(self)
		self.name = "REVIEWED"
		self.specie = 'verbs'
		self.basic = "review"
		self.jsondata = {}
