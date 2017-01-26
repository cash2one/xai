

from xai.brain.wordbase.nouns._homonym import _HOMONYM

#calss header
class _HOMONYMS(_HOMONYM, ):
	def __init__(self,): 
		_HOMONYM.__init__(self)
		self.name = "HOMONYMS"
		self.specie = 'nouns'
		self.basic = "homonym"
		self.jsondata = {}
