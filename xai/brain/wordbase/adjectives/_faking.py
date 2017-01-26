

from xai.brain.wordbase.adjectives._fake import _FAKE

#calss header
class _FAKING(_FAKE, ):
	def __init__(self,): 
		_FAKE.__init__(self)
		self.name = "FAKING"
		self.specie = 'adjectives'
		self.basic = "fake"
		self.jsondata = {}
