

from xai.brain.wordbase.nouns._overpass import _OVERPASS

#calss header
class _OVERPASSES(_OVERPASS, ):
	def __init__(self,): 
		_OVERPASS.__init__(self)
		self.name = "OVERPASSES"
		self.specie = 'nouns'
		self.basic = "overpass"
		self.jsondata = {}
