

from xai.brain.wordbase.nouns._claimant import _CLAIMANT

#calss header
class _CLAIMANTS(_CLAIMANT, ):
	def __init__(self,): 
		_CLAIMANT.__init__(self)
		self.name = "CLAIMANTS"
		self.specie = 'nouns'
		self.basic = "claimant"
		self.jsondata = {}
