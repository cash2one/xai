

from xai.brain.wordbase.nouns._occupant import _OCCUPANT

#calss header
class _OCCUPANTS(_OCCUPANT, ):
	def __init__(self,): 
		_OCCUPANT.__init__(self)
		self.name = "OCCUPANTS"
		self.specie = 'nouns'
		self.basic = "occupant"
		self.jsondata = {}
