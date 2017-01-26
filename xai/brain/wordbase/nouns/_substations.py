

from xai.brain.wordbase.nouns._substation import _SUBSTATION

#calss header
class _SUBSTATIONS(_SUBSTATION, ):
	def __init__(self,): 
		_SUBSTATION.__init__(self)
		self.name = "SUBSTATIONS"
		self.specie = 'nouns'
		self.basic = "substation"
		self.jsondata = {}
