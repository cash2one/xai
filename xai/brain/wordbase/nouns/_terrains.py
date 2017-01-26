

from xai.brain.wordbase.nouns._terrain import _TERRAIN

#calss header
class _TERRAINS(_TERRAIN, ):
	def __init__(self,): 
		_TERRAIN.__init__(self)
		self.name = "TERRAINS"
		self.specie = 'nouns'
		self.basic = "terrain"
		self.jsondata = {}
