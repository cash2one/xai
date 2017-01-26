

from xai.brain.wordbase.nouns._gazetteer import _GAZETTEER

#calss header
class _GAZETTEERS(_GAZETTEER, ):
	def __init__(self,): 
		_GAZETTEER.__init__(self)
		self.name = "GAZETTEERS"
		self.specie = 'nouns'
		self.basic = "gazetteer"
		self.jsondata = {}
