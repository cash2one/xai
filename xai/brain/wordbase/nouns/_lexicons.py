

from xai.brain.wordbase.nouns._lexicon import _LEXICON

#calss header
class _LEXICONS(_LEXICON, ):
	def __init__(self,): 
		_LEXICON.__init__(self)
		self.name = "LEXICONS"
		self.specie = 'nouns'
		self.basic = "lexicon"
		self.jsondata = {}
