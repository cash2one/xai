

from xai.brain.wordbase.nouns._hoax import _HOAX

#calss header
class _HOAXED(_HOAX, ):
	def __init__(self,): 
		_HOAX.__init__(self)
		self.name = "HOAXED"
		self.specie = 'nouns'
		self.basic = "hoax"
		self.jsondata = {}
