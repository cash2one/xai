

from xai.brain.wordbase.nouns._suffix import _SUFFIX

#calss header
class _SUFFIXES(_SUFFIX, ):
	def __init__(self,): 
		_SUFFIX.__init__(self)
		self.name = "SUFFIXES"
		self.specie = 'nouns'
		self.basic = "suffix"
		self.jsondata = {}
