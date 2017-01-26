

from xai.brain.wordbase.nouns._acronym import _ACRONYM

#calss header
class _ACRONYMS(_ACRONYM, ):
	def __init__(self,): 
		_ACRONYM.__init__(self)
		self.name = "ACRONYMS"
		self.specie = 'nouns'
		self.basic = "acronym"
		self.jsondata = {}
