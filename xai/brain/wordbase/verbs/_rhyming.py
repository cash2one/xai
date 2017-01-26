

from xai.brain.wordbase.verbs._rhyme import _RHYME

#calss header
class _RHYMING(_RHYME, ):
	def __init__(self,): 
		_RHYME.__init__(self)
		self.name = "RHYMING"
		self.specie = 'verbs'
		self.basic = "rhyme"
		self.jsondata = {}
