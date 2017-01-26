

from xai.brain.wordbase.nouns._coolant import _COOLANT

#calss header
class _COOLANTS(_COOLANT, ):
	def __init__(self,): 
		_COOLANT.__init__(self)
		self.name = "COOLANTS"
		self.specie = 'nouns'
		self.basic = "coolant"
		self.jsondata = {}
