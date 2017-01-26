

from xai.brain.wordbase.verbs._scramble import _SCRAMBLE

#calss header
class _SCRAMBLED(_SCRAMBLE, ):
	def __init__(self,): 
		_SCRAMBLE.__init__(self)
		self.name = "SCRAMBLED"
		self.specie = 'verbs'
		self.basic = "scramble"
		self.jsondata = {}
