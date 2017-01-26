

from xai.brain.wordbase.nouns._profanity import _PROFANITY

#calss header
class _PROFANITIES(_PROFANITY, ):
	def __init__(self,): 
		_PROFANITY.__init__(self)
		self.name = "PROFANITIES"
		self.specie = 'nouns'
		self.basic = "profanity"
		self.jsondata = {}
