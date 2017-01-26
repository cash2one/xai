

from xai.brain.wordbase.nouns._rhyme import _RHYME

#calss header
class _RHYMING(_RHYME, ):
	def __init__(self,): 
		_RHYME.__init__(self)
		self.name = "RHYMING"
		self.specie = 'nouns'
		self.basic = "rhyme"
		self.jsondata = {}
