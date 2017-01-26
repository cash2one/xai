

from xai.brain.wordbase.nouns._postmark import _POSTMARK

#calss header
class _POSTMARKED(_POSTMARK, ):
	def __init__(self,): 
		_POSTMARK.__init__(self)
		self.name = "POSTMARKED"
		self.specie = 'nouns'
		self.basic = "postmark"
		self.jsondata = {}
