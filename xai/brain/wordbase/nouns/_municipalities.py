

from xai.brain.wordbase.nouns._municipality import _MUNICIPALITY

#calss header
class _MUNICIPALITIES(_MUNICIPALITY, ):
	def __init__(self,): 
		_MUNICIPALITY.__init__(self)
		self.name = "MUNICIPALITIES"
		self.specie = 'nouns'
		self.basic = "municipality"
		self.jsondata = {}
