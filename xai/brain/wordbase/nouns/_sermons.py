

from xai.brain.wordbase.nouns._sermon import _SERMON

#calss header
class _SERMONS(_SERMON, ):
	def __init__(self,): 
		_SERMON.__init__(self)
		self.name = "SERMONS"
		self.specie = 'nouns'
		self.basic = "sermon"
		self.jsondata = {}
