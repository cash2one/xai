

from xai.brain.wordbase.nouns._gray import _GRAY

#calss header
class _GRAYED(_GRAY, ):
	def __init__(self,): 
		_GRAY.__init__(self)
		self.name = "GRAYED"
		self.specie = 'nouns'
		self.basic = "gray"
		self.jsondata = {}
