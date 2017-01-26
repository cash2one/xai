

from xai.brain.wordbase.nouns._pad import _PAD

#calss header
class _PADS(_PAD, ):
	def __init__(self,): 
		_PAD.__init__(self)
		self.name = "PADS"
		self.specie = 'nouns'
		self.basic = "pad"
		self.jsondata = {}
