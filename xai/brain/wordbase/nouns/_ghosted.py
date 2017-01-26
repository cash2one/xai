

from xai.brain.wordbase.nouns._ghost import _GHOST

#calss header
class _GHOSTED(_GHOST, ):
	def __init__(self,): 
		_GHOST.__init__(self)
		self.name = "GHOSTED"
		self.specie = 'nouns'
		self.basic = "ghost"
		self.jsondata = {}
