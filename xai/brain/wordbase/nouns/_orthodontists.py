

from xai.brain.wordbase.nouns._orthodontist import _ORTHODONTIST

#calss header
class _ORTHODONTISTS(_ORTHODONTIST, ):
	def __init__(self,): 
		_ORTHODONTIST.__init__(self)
		self.name = "ORTHODONTISTS"
		self.specie = 'nouns'
		self.basic = "orthodontist"
		self.jsondata = {}
