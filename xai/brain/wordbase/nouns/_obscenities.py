

from xai.brain.wordbase.nouns._obscenity import _OBSCENITY

#calss header
class _OBSCENITIES(_OBSCENITY, ):
	def __init__(self,): 
		_OBSCENITY.__init__(self)
		self.name = "OBSCENITIES"
		self.specie = 'nouns'
		self.basic = "obscenity"
		self.jsondata = {}
