

from xai.brain.wordbase.nouns._fake import _FAKE

#calss header
class _FAKES(_FAKE, ):
	def __init__(self,): 
		_FAKE.__init__(self)
		self.name = "FAKES"
		self.specie = 'nouns'
		self.basic = "fake"
		self.jsondata = {}
