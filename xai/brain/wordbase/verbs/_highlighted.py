

from xai.brain.wordbase.verbs._highlight import _HIGHLIGHT

#calss header
class _HIGHLIGHTED(_HIGHLIGHT, ):
	def __init__(self,): 
		_HIGHLIGHT.__init__(self)
		self.name = "HIGHLIGHTED"
		self.specie = 'verbs'
		self.basic = "highlight"
		self.jsondata = {}
