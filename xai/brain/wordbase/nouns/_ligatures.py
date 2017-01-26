

from xai.brain.wordbase.nouns._ligature import _LIGATURE

#calss header
class _LIGATURES(_LIGATURE, ):
	def __init__(self,): 
		_LIGATURE.__init__(self)
		self.name = "LIGATURES"
		self.specie = 'nouns'
		self.basic = "ligature"
		self.jsondata = {}
