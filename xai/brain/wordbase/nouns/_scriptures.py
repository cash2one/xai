

from xai.brain.wordbase.nouns._scripture import _SCRIPTURE

#calss header
class _SCRIPTURES(_SCRIPTURE, ):
	def __init__(self,): 
		_SCRIPTURE.__init__(self)
		self.name = "SCRIPTURES"
		self.specie = 'nouns'
		self.basic = "scripture"
		self.jsondata = {}
