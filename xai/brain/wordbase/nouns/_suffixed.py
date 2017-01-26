

from xai.brain.wordbase.nouns._suffix import _SUFFIX

#calss header
class _SUFFIXED(_SUFFIX, ):
	def __init__(self,): 
		_SUFFIX.__init__(self)
		self.name = "SUFFIXED"
		self.specie = 'nouns'
		self.basic = "suffix"
		self.jsondata = {}
