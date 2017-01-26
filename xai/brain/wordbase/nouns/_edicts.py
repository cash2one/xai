

from xai.brain.wordbase.nouns._edict import _EDICT

#calss header
class _EDICTS(_EDICT, ):
	def __init__(self,): 
		_EDICT.__init__(self)
		self.name = "EDICTS"
		self.specie = 'nouns'
		self.basic = "edict"
		self.jsondata = {}
