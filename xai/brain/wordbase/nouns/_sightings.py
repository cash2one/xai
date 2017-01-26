

from xai.brain.wordbase.nouns._sighting import _SIGHTING

#calss header
class _SIGHTINGS(_SIGHTING, ):
	def __init__(self,): 
		_SIGHTING.__init__(self)
		self.name = "SIGHTINGS"
		self.specie = 'nouns'
		self.basic = "sighting"
		self.jsondata = {}
