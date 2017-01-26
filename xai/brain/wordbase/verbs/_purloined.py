

from xai.brain.wordbase.verbs._purloin import _PURLOIN

#calss header
class _PURLOINED(_PURLOIN, ):
	def __init__(self,): 
		_PURLOIN.__init__(self)
		self.name = "PURLOINED"
		self.specie = 'verbs'
		self.basic = "purloin"
		self.jsondata = {}
