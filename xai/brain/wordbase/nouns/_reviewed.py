

from xai.brain.wordbase.nouns._review import _REVIEW

#calss header
class _REVIEWED(_REVIEW, ):
	def __init__(self,): 
		_REVIEW.__init__(self)
		self.name = "REVIEWED"
		self.specie = 'nouns'
		self.basic = "review"
		self.jsondata = {}
