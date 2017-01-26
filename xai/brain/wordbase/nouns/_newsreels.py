

from xai.brain.wordbase.nouns._newsreel import _NEWSREEL

#calss header
class _NEWSREELS(_NEWSREEL, ):
	def __init__(self,): 
		_NEWSREEL.__init__(self)
		self.name = "NEWSREELS"
		self.specie = 'nouns'
		self.basic = "newsreel"
		self.jsondata = {}
