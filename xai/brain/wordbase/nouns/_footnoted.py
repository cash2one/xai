

from xai.brain.wordbase.nouns._footnote import _FOOTNOTE

#calss header
class _FOOTNOTED(_FOOTNOTE, ):
	def __init__(self,): 
		_FOOTNOTE.__init__(self)
		self.name = "FOOTNOTED"
		self.specie = 'nouns'
		self.basic = "footnote"
		self.jsondata = {}
