

from xai.brain.wordbase.nouns._screenplay import _SCREENPLAY

#calss header
class _SCREENPLAYS(_SCREENPLAY, ):
	def __init__(self,): 
		_SCREENPLAY.__init__(self)
		self.name = "SCREENPLAYS"
		self.specie = 'nouns'
		self.basic = "screenplay"
		self.jsondata = {}
