

from xai.brain.wordbase.verbs._rhyme import _RHYME

#calss header
class _RHYMED(_RHYME, ):
	def __init__(self,): 
		_RHYME.__init__(self)
		self.name = "RHYMED"
		self.specie = 'verbs'
		self.basic = "rhyme"
		self.jsondata = {}
