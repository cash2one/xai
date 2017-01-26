

from xai.brain.wordbase.nouns._artist import _ARTIST

#calss header
class _ARTISTS(_ARTIST, ):
	def __init__(self,): 
		_ARTIST.__init__(self)
		self.name = "ARTISTS"
		self.specie = 'nouns'
		self.basic = "artist"
		self.jsondata = {}
