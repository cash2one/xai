

from xai.brain.wordbase.nouns._surgeon import _SURGEON

#calss header
class _SURGEONS(_SURGEON, ):
	def __init__(self,): 
		_SURGEON.__init__(self)
		self.name = "SURGEONS"
		self.specie = 'nouns'
		self.basic = "surgeon"
		self.jsondata = {}
