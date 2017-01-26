

from xai.brain.wordbase.nouns._rhyme import _RHYME

#calss header
class _RHYMED(_RHYME, ):
	def __init__(self,): 
		_RHYME.__init__(self)
		self.name = "RHYMED"
		self.specie = 'nouns'
		self.basic = "rhyme"
		self.jsondata = {}
