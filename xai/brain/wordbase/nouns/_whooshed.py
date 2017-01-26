

from xai.brain.wordbase.nouns._whoosh import _WHOOSH

#calss header
class _WHOOSHED(_WHOOSH, ):
	def __init__(self,): 
		_WHOOSH.__init__(self)
		self.name = "WHOOSHED"
		self.specie = 'nouns'
		self.basic = "whoosh"
		self.jsondata = {}
