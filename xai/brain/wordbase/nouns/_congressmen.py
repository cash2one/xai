

from xai.brain.wordbase.nouns._congressman import _CONGRESSMAN

#calss header
class _CONGRESSMEN(_CONGRESSMAN, ):
	def __init__(self,): 
		_CONGRESSMAN.__init__(self)
		self.name = "CONGRESSMEN"
		self.specie = 'nouns'
		self.basic = "congressman"
		self.jsondata = {}
