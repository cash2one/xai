

from xai.brain.wordbase.nouns._silencer import _SILENCER

#calss header
class _SILENCERS(_SILENCER, ):
	def __init__(self,): 
		_SILENCER.__init__(self)
		self.name = "SILENCERS"
		self.specie = 'nouns'
		self.basic = "silencer"
		self.jsondata = {}
