

from xai.brain.wordbase.nouns._spotlight import _SPOTLIGHT

#calss header
class _SPOTLIGHTED(_SPOTLIGHT, ):
	def __init__(self,): 
		_SPOTLIGHT.__init__(self)
		self.name = "SPOTLIGHTED"
		self.specie = 'nouns'
		self.basic = "spotlight"
		self.jsondata = {}
