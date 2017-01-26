

from xai.brain.wordbase.nouns._inmate import _INMATE

#calss header
class _INMATES(_INMATE, ):
	def __init__(self,): 
		_INMATE.__init__(self)
		self.name = "INMATES"
		self.specie = 'nouns'
		self.basic = "inmate"
		self.jsondata = {}
