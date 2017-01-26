

from xai.brain.wordbase.nouns._defendant import _DEFENDANT

#calss header
class _DEFENDANTS(_DEFENDANT, ):
	def __init__(self,): 
		_DEFENDANT.__init__(self)
		self.name = "DEFENDANTS"
		self.specie = 'nouns'
		self.basic = "defendant"
		self.jsondata = {}
