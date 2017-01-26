

from xai.brain.wordbase.nouns._label import _LABEL

#calss header
class _LABELLED(_LABEL, ):
	def __init__(self,): 
		_LABEL.__init__(self)
		self.name = "LABELLED"
		self.specie = 'nouns'
		self.basic = "label"
		self.jsondata = {}
