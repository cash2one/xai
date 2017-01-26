

from xai.brain.wordbase.nouns._lyricist import _LYRICIST

#calss header
class _LYRICISTS(_LYRICIST, ):
	def __init__(self,): 
		_LYRICIST.__init__(self)
		self.name = "LYRICISTS"
		self.specie = 'nouns'
		self.basic = "lyricist"
		self.jsondata = {}
