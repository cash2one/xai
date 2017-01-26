

from xai.brain.wordbase.nouns._citation import _CITATION

#calss header
class _CITATIONS(_CITATION, ):
	def __init__(self,): 
		_CITATION.__init__(self)
		self.name = "CITATIONS"
		self.specie = 'nouns'
		self.basic = "citation"
		self.jsondata = {}
