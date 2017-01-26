

from xai.brain.wordbase.nouns._epithet import _EPITHET

#calss header
class _EPITHETS(_EPITHET, ):
	def __init__(self,): 
		_EPITHET.__init__(self)
		self.name = "EPITHETS"
		self.specie = 'nouns'
		self.basic = "epithet"
		self.jsondata = {}
