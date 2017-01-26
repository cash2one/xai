

from xai.brain.wordbase.nouns._scramble import _SCRAMBLE

#calss header
class _SCRAMBLED(_SCRAMBLE, ):
	def __init__(self,): 
		_SCRAMBLE.__init__(self)
		self.name = "SCRAMBLED"
		self.specie = 'nouns'
		self.basic = "scramble"
		self.jsondata = {}
